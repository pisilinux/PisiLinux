#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "NEWS") 
    pisitools.removeDir("/usr/share/appdata/")
    pisitools.removeDir("/usr/share/gnome-clocks/")
    pisitools.removeDir("/usr/share/icons/")
    pisitools.removeDir("/usr/share/help/")
    