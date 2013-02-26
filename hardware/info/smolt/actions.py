#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    shelltools.cd("client")
    autotools.make()

def install():
    shelltools.cd("client")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.rename("/etc/smolt/config.py",
                     "smolt.cfg")
    pisitools.remove("/usr/share/smolt/client/config.py")
    pisitools.dosym("/etc/smolt/smolt.cfg",
                    "/usr/share/smolt/client/config.py")

    # Stupid makefile links executables to wrong place.Remove and link them again.
    pisitools.dosym("/usr/share/smolt/client/sendProfile.py",
                    "/usr/bin/smoltSendProfile")
    pisitools.dosym("/usr/share/smolt/client/deleteProfile.py",
                    "/usr/bin/smoltDeleteProfile")
    pisitools.dosym("/usr/share/smolt/client/smoltGui.py",
                    "/usr/bin/smoltGui")


    shelltools.touch("%s/etc/smolt/pub-uuid-smolt.pardus.org.tr" % get.installDIR())
    shelltools.chmod("%s/etc/smolt/pub-uuid-smolt.pardus.org.tr" % get.installDIR(), 0666)
    shelltools.touch("%s/etc/smolt/smolt-token-smolt.pardus.org.tr" % get.installDIR())
    shelltools.chmod("%s/etc/smolt/smolt-token-smolt.pardus.org.tr" % get.installDIR(), 0666)
    shelltools.touch("%s/etc/smolt/uuiddb.cfg" % get.installDIR())
    shelltools.chmod("%s/etc/smolt/uuiddb.cfg" % get.installDIR(), 0666)
