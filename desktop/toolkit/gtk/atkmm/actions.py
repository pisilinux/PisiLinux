#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static")
    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.domove("/usr/share/doc/%s-1.6/*" % get.srcNAME(), "/usr/share/gtk-doc/html/atkmm")
    pisitools.removeDir("/usr/share/doc/%s-1.6" % get.srcNAME())
    pisitools.removeDir("/usr/share/devhelp")

    pisitools.dodoc("ChangeLog", "COPYING", "NEWS", "README")
