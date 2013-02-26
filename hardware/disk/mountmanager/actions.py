#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="mm"

def setup():
    pisitools.dosed("configure", "Exec=mm", "Exec=mountmanager")
    autotools.rawConfigure("--prefix=/usr \
                            --datadir=/usr/share \
                            --include_path=/usr/include \
                            --lib_path=/usr/lib")

def build():
    autotools.make()

def install():
    pisitools.dobin("mountmanager")
    pisitools.dobin("mm")

    pisitools.insinto("/usr/lib/mountmanager/plugins", "plugins/*/*.so")
    pisitools.insinto("/usr/lib/mountmanager/trans", "trans/*.qm")

    pisitools.insinto("/usr/share/applications", "resources/desktop/*.desktop")
    pisitools.insinto("/usr/share/icons", "resources/desktop/mm.png")

    pisitools.dodoc("license", "readme.en")
    #pisitools.dodoc("doc/*/*")
    pisitools.doman("mans/*")

    pisitools.insinto("/usr/share/mountmanager/icons", "resources/icons/*.png")
    pisitools.insinto("/usr/share/mountmanager/options", "options/*.xml")
    pisitools.insinto("/usr/share/mountmanager/images", "resources/images/*.html")
