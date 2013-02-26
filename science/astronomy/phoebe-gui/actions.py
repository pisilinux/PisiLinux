#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir="phoebe-gui-%s" % get.srcVERSION()

def setup():
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
