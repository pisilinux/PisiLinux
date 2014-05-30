# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

options="WXPORT=gtk2 UNICODE=1 WX_CONFIG=/usr/bin/wx-config-2.8"

def setup():
    autotools.configure("--with-gtk=2 \
                         --with-opengl \
                         --with-sdl \
                         --enable-unicode \
                         --enable-graphics_ctx \
                         --disable-optimize \
                         --enable-mediactrl \
                         --with-regex=sys --with-libpng=sys \
                         --with-libxpm=sys --with-libjpeg=sys \
                         --with-libtiff=sys --disable-precomp-headers")

def build():
    shelltools.cd("wxPython")
    pythonmodules.compile(options)

def install():
    shelltools.cd("wxPython")
    pythonmodules.install(options)

    pisitools.dohtml("docs/*")
    pisitools.dodoc("docs/*.txt")
