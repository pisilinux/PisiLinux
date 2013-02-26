# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")
    autotools.autoreconf("-fi")
    autotools.configure("--with-frontend=qt4 \
                         --without-aspell \
                         --with-enchant \
                         --with-hunspell \
                         --enable-build-type=release \
                         --without-included-boost \
                         --without-included-mythes \
                         --disable-stdlib-debug \
                         --disable-rpath")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps/", "lib/images/lyx.png")

    pisitools.dodoc("ANNOUNCE", "COPYING", "RELEASE-NOTES", "README", "NEWS")
