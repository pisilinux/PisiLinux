#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "GPL*", "TODO")
