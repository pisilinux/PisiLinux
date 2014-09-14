#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
#    pisitools.domo("po/tr.po", "tr", "gnujump.mo")
    pisitools.insinto("/usr/share/pixmaps", "skins/xjump/hero1.0.png", "gnujump.png")

    pisitools.dodoc("AUTHORS", "README", "COPYING")
