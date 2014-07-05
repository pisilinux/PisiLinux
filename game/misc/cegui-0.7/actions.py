#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./bootstrap")
    shelltools.system('Lua_CFLAGS="$(pkg-config --cflags lua5.1)" \
                       Lua_LIBS="$(pkg-config --libs lua5.1)" \
                       PYTHON="/usr/bin/python2.7" ./configure --prefix=/usr --sysconfdir=/etc \
                       --enable-null-renderer --with-gtk2 --disable-samples \
                       --disable-ogre-renderer --disable-irrlicht-renderer')       

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("doc/COPYING", "doc/TinyXML-License", "doc/GLEW-LICENSE","doc/PCRE-LICENSE", "doc/README", "doc/stringencoders-license")