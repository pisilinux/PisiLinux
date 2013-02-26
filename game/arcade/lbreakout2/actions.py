#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure('--enable-sdl-net \
                         --localstatedir=/usr/share/lbreakout2 \
                         --with-docdir="/%s/%s/html"' % (get.docDIR(), get.srcNAME()))
def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "client/gfx/win_icon.png", "lbreakout2.png")
    pisitools.remove("/usr/share/icons/lbreakout48.gif")
    pisitools.removeDir("/usr/share/icons")

    pisitools.domo("po/tr.po", "tr", "lbreakout2.mo")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")
