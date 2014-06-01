from comar.service import *
import os

serviceType = "server"
serviceDefault = "off"
serviceDesc = _({"en": "OpenVPN",
                 "tr": "OpenVPN"})


OPENVPN = "/usr/sbin/openvpn"
PIDDIR = "/run/openvpn"
WORKDIR = "/etc/openvpn"
PIDFILE = ""


MSG_NOCONF = _({"en": "%s doesn't contain any OpenVPN configuration file." % WORKDIR,
                "tr": "%s herhangi bir OpenVPN yapılandırma dosyası içermiyor." % WORKDIR,
                })

@synchronized
def start():
    # Load tun
    os.system("modprobe -q tun")

    # Run startup script if defined
    if os.path.exists(os.path.join(WORKDIR, "openvpn-startup.sh")):
        os.system(os.path.join(WORKDIR, "openvpn-startup.sh"))

    configs = [_c for _c in os.listdir(WORKDIR) if _c.endswith(".conf")]

    if len(configs) > 0:
        # There's at least 1 OpenVPN configuration to start

        # Start every .conf in WORKDIR and run .sh if it exists
        for conf in configs:
            conf_name = conf.split(".conf")[0]
            sh_name = os.path.join(WORKDIR, "%s.sh" % conf_name)
            PIDFILE = os.path.join(PIDDIR, "%s.pid" % conf_name)

            if os.path.exists(sh_name):
                os.system(sh_name)

            # Clean stale pid files
            if os.path.exists(PIDFILE):
                os.unlink(PIDFILE)

            startService(command=OPENVPN,
                         args="--daemon --writepid %s --config %s/%s --cd %s --script-security 2" % (PIDFILE, WORKDIR, conf, WORKDIR),
                         pidfile=PIDFILE,
                         donotify=True)

        # Reset PIDFILE. This is a hack for status() calls from startService() problems..
        PIDFILE = ""
    else:
        fail(MSG_NOCONF)

@synchronized
def stop():
    for pidf in [pid for pid in os.listdir(PIDDIR) if pid.endswith(".pid")]:
        stopService(pidfile="%s/%s" % (PIDDIR, pidf),
                    donotify=True)

        try:
            os.unlink(os.path.join(PIDDIR, pidf))
        except OSError:
            pass

    # Run shutdown script if defined
    if os.path.exists(os.path.join(WORKDIR, "openvpn-shutdown.sh")):
        os.system(os.path.join(WORKDIR, "openvpn-shutdown.sh"))

@synchronized
def reload():
    import signal
    for pidf in [pid for pid in os.listdir(PIDDIR) if pid.endswith(".pid")]:
        stopService(pidfile="%s/%s" % (PIDDIR, pidf),
                    signalno=signal.SIGHUP,
                    donotify=True)


def status():
    if PIDFILE:
        return isServiceRunning(pidfile=PIDFILE)
    else:
        state = False
        for pidf in [pid for pid in os.listdir(PIDDIR) if pid.endswith(".pid")]:
            PIDFILE = os.path.join(PIDDIR, pidf)
            state = state and isServiceRunning(pidfile=PIDFILE)
        return state

