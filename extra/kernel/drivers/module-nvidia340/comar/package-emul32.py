#!/usr/bin/python

import os

driver_dir_name = "nvidia340"
libdir = "/usr/lib32/%s" % driver_dir_name
datadir = "/usr/share/%s" % driver_dir_name

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system(" /usr/sbin/alternatives \
                --install   /usr/lib32/libGL.so.1.2.0               libGL-32bit                  %(libdir)s/libGL.so.1.2.0     50 \
                --slave     /usr/lib32/xorg/modules/volatile        xorg-modules-volatile-32bit  %(libdir)s/modules"
                % {"libdir": libdir, "datadir": datadir})
#                --slave     /etc/ld.so.conf.d/10-nvidia-32bit.conf  nvidia-ldsoconf-32bit        %(datadir)s/32bit-ld.so.conf"

    # If this driver is in use, refresh links after installation.
    if os.readlink("/etc/alternatives/libGL-32bit") == "%s/libGL.so.1.2.0" % libdir:
        os.system("/usr/sbin/alternatives --set libGL-32bit %s/libGL.so.1.2.0" % libdir)
        os.system("/sbin/ldconfig -X")

def preRemove():
    # FIXME This is not needed when upgrading package; but pisi does not
    #       provide a way to learn operation type.
    #os.system("/usr/sbin/alternatives --remove libGL-32bit %s/libGL.so.1.2.0" % libdir)
    pass
