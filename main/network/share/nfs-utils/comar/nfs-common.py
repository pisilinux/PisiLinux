# -*- coding: utf-8 -*-
from comar.service import *
from pardus import fstabutils
import os

serviceType = "server"
serviceDesc = _({"en": "NFS Common Services",
                 "tr": "NFS Ortak Servisleri"})

serviceConf = "nfs"

ERR_INSMOD = _({"en": "Failed probing module %s",
               "tr": "%s modülü yüklenemedi",
             })

ERR_RMMOD = _({"en": "Failed removing module %s",
                "tr": "%s modülü çıkarılamadı",
              })

PIPEFS_MOUNTPOINT = "/var/lib/nfs/rpc_pipefs"

STATD_PIDFILE = "/run/rpc.statd.pid"
IDMAPD_PIDFILE = "/run/rpc.idmapd.pid"
GSSD_PIDFILE = "/run/rpc.gssd.pid"

# Parse the fstab file and determine whether we need gssd or not, by searching
# mount option sec=krb* in nfs mount entries.
# If none, nfs conf.d file decides if it's needed.
def need_gssd():
    fstab = fstabutils.Fstab()
    for entry in fstab.get_entries():
        if entry.is_nfs():
            if "sec=krb" in entry.get_fs_mntopts():
                return True

@synchronized
def start():
    startDependencies("rpcbind")

    # Set the ports lockd should listen on
    LOCKD_TCPPORT = config.get("LOCKD_TCPPORT")
    if LOCKD_TCPPORT:
        run("/sbin/sysctl -w fs.nfs.nlm_tcpport=%s" % LOCKD_TCPPORT)

    LOCKD_UDPPORT = config.get("LOCKD_UDPPORT")
    if LOCKD_UDPPORT:
        run("/sbin/sysctl -w fs.nfs.nlm_udpport=%s" % LOCKD_UDPPORT)

    # rpc.statd is first
    RPCSTATD_OPTIONS = config.get("RPCSTATD_OPTIONS", "")
    STATD_PORT = config.get("STATD_PORT")
    if STATD_PORT:
        RPCSTATD_OPTIONS += " -p %s" % STATD_PORT

    startService(command="/sbin/rpc.statd",
                 args="%s" % RPCSTATD_OPTIONS,
                 donotify=True,
                 pidfile=STATD_PIDFILE)

    if config.get("NEED_IDMAPD", "yes") == "yes" or (config.get("NEED_GSSD", "no") == "yes" or need_gssd()):
        if run("/sbin/modprobe -q nfs"):
            fail(ERR_INSMOD % "nfs")

        # Make sure the mointpoint exists
        if not os.path.exists(PIPEFS_MOUNTPOINT):
            os.makedirs(PIPEFS_MOUNTPOINT)

        # Check if PIPEFS_MOUNTPOINT is a real mounted fs
        if run("/bin/mountpoint -q %s" % PIPEFS_MOUNTPOINT):
            run("/bin/mount -t rpc_pipefs rpc_pipefs %s" % PIPEFS_MOUNTPOINT)

        startService(command="/usr/sbin/rpc.idmapd",
                     args="-f %s" % config.get("RPCIDMAPD_OPTIONS", ""),
                     donotify=True,
                     detach=True,
                     makepid=True,
                     pidfile=IDMAPD_PIDFILE)

        if config.get("NEED_GSSD", "no") == "yes" or need_gssd():
            if run("/sbin/modprobe -q rpcsec_gss_krb5"):
                fail(ERR_INSMOD % "rpcsec_gss_krb5")

            startService(command="/usr/sbin/rpc.gssd",
                         args="-f %s" % config.get("RPCGSSD_OPTIONS", ""),
                         donotify=True,
                         detach=True,
                         makepid=True,
                         pidfile=GSSD_PIDFILE)

@synchronized
def stop():
    LOCKD_TCPPORT = config.get("LOCKD_TCPPORT")
    if LOCKD_TCPPORT:
        run("/sbin/sysctl -w fs.nfs.nlm_tcpport=0")

    LOCKD_UDPPORT = config.get("LOCKD_UDPPORT")
    if LOCKD_UDPPORT:
        run("/sbin/sysctl -w fs.nfs.nlm_udpport=0")

    stopService(pidfile=GSSD_PIDFILE,
                donotify=True)

    stopService(pidfile=IDMAPD_PIDFILE,
                donotify=True)

    stopService(pidfile=STATD_PIDFILE,
                donotify=True)

    if not run("/bin/mountpoint -q %s" % PIPEFS_MOUNTPOINT):
        run("/bin/umount %s" % PIPEFS_MOUNTPOINT)

def status():
    result = isServiceRunning(STATD_PIDFILE)
    if config.get("NEED_IDMAPD", "yes") == "yes":
        result = result and isServiceRunning(IDMAPD_PIDFILE)
    if config.get("NEED_GSSD", "no") == "yes" or need_gssd():
        result = result and isServiceRunning(GSSD_PIDFILE)
    return result
