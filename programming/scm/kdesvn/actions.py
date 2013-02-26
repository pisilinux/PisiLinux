#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

shelltools.export("HOME", "%s" % get.workDIR())

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #Remove files conflicts with kdesdk(cervisia)
    pisitools.remove("usr/share/kde4/services/svn*.protocol")

    #Remove duplicate files with libsvnqt
    pisitools.remove("/usr/lib/libsvnqt.so*")
    pisitools.removeDir("/usr/include/")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "GPL*", "TODO")
