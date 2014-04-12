#!/usr/bin/python

import os

libdir = "/usr/lib/fglrx"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/sbin/alternatives \
                --install   /usr/lib/libGL.so.1.2.0           libGL                   %(libdir)s/libGL.so.1.2.0     50 \
                --slave     /usr/lib/xorg/modules/volatile  xorg-modules-volatile   %(libdir)s/modules"
              % {"libdir": libdir})

def preRemove():
    # FIXME This is not needed when upgrading package; but pisi does not
    #       provide a way to learn operation type.
    #os.system("/usr/sbin/alternatives --remove libGL %s/libGL.so.1.2" % libdir)
    pass
