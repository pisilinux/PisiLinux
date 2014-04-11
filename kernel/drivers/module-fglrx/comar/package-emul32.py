#!/usr/bin/python

import os

libdir = "/usr/lib32/fglrx"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/sbin/alternatives \
                --install   /usr/lib32/libGL.so.1.2.0 libGL-32bit %(libdir)s/libGL.so.1.2.0     50 \
                --slave     /usr/lib32/xorg/modules/volatile  xorg-modules-volatile-32bit   %(libdir)s/modules"
              % {"libdir": libdir})

def preRemove():
    # FIXME This is not needed when upgrading package; but pisi does not
    #       provide a way to learn operation type.
    #os.system("/usr/sbin/alternatives --remove libGL-32bit %s/libGL.so.1.2" % libdir)
    pass

