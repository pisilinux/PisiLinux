#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

#WorkDir="phoebe-gui-%s" % get.srcVERSION()

def setup():
    pisitools.ldflags.add("-lm")
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dobin("src/phoebe-gui")
    
    pisitools.insinto("/usr/share/phoebe/gui/glade/", "glade/phoebe*")
    pisitools.insinto("/usr/share/applications/", "phoebe-gui.desktop")
    pisitools.insinto("/usr/share/mime-info/", "phoebe-gui.mime")
    pisitools.insinto("/usr/share/mime/packages/", "phoebe-gui.xml")
    pisitools.insinto("/usr/share/phoebe/gui/pixmaps/", "pixmaps/detach.png")
    pisitools.insinto("/usr/share/phoebe/gui/pixmaps/", "pixmaps/ico.png")
    pisitools.insinto("/usr/share/pixmaps/", "pixmaps/phoebe-gui.png")
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
