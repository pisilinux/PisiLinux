#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.cd("..")
    shelltools.cd("kde4") 
    autotools.configure()
    shelltools.cd("..")
    shelltools.cd("common") 
    autotools.configure()
    shelltools.cd("..")

def build():
    shelltools.cd("..")
    shelltools.cd("kde4")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("common")
    autotools.make()
    shelltools.cd("..")

def install(): 
    shelltools.cd("..")
    shelltools.cd("kde4")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")
    shelltools.cd("common")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")
    
    pisitools.removeDir("/etc")
    pisitools.removeDir("/usr/share/doc/kde")
    pisitools.remove("/usr/bin/backintime-askpass")