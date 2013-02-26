#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-sound \
                         --enable-SDL \
                         --enable-nvidia=no")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "README.FONTS")
    pisitools.doman("foobillard.6")
    pisitools.insinto("/usr/share/pixmaps", "data/full_symbol.png", "foobillard.png")

