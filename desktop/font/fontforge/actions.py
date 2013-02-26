#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "fontforge-%s-b" % get.srcVERSION().split('_')[-1]

def setup():
    libtools.libtoolize()
    autotools.aclocal()
    autotools.autoconf()

    autotools.configure("--with-freetype-bytecode=no \
                         --with-regular-link \
                         --enable-pyextension")

    pisitools.dosed('libtool', '^hardcode_libdir_flag_spec=.*', 'hardcode_libdir_flag_spec=""')
    pisitools.dosed('libtool', '^runpath_var=LD_RUN_PATH', 'runpath_var=DIE_RPATH_DIE')

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/applications", "Packaging/fontforge.desktop")
    #pisitools.insinto("/usr/share/pixmaps", "Packaging/fontforge.png")
    pisitools.insinto("/usr/share/mime/packages", "Packaging/fontforge.xml")

    shelltools.cd("pyhook")
    pythonmodules.install()

    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "LICENSE", "README*")

