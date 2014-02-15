#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("data/easytag.desktop.in", "Icon=easytag", "Icon=/usr/share/pixmaps/easytag.png")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        
    pisitools.dodoc("TODO", "COPYING", "README", "ChangeLog", "THANKS")
        
    pisitools.insinto("/usr/share/pixmaps/", "data/icons/48x48/easytag.png")