#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

major = ".".join(get.srcVERSION().split(".")[:2])

def setup():
    pisitools.dosed("src/Makefile", "^CFLAGS.*$", "CFLAGS=%s -fPIC -DLUA_USE_LINUX" % get.CFLAGS())
    pisitools.dosed("src/Makefile", "^MYLDFLAGS.*$", "MYLDFLAGS=%s" % get.LDFLAGS())
    #pisitools.dosed("lua.pc", "%VER%", "%s" % get.srcVERSION())
    #pisitools.dosed("lua.pc", "%REL%", "%s" % get.srcVERSION())

def build():
    autotools.make("linux")

def install():
    autotools.rawInstall("INSTALL_TOP=%s/usr" % get.installDIR())
    pisitools.dosym("/usr/lib/liblua.so.5.1", "/usr/lib/liblua.so")
    pisitools.insinto("/usr/share/lua/5.1", "etc/strict.lua")
    pisitools.insinto("/usr/share/lua/5.1", "test/*.lua")
    pisitools.insinto("/usr/lib/pkgconfig/5.1", "etc/lua.pc")

    pisitools.domove("/usr/include/lua.h", "usr/include/5.1")
    pisitools.domove("/usr/include/lua.hpp", "usr/include/5.1")
    pisitools.domove("/usr/include/luaconf.h", "usr/include/5.1")
    pisitools.domove("/usr/include/lualib.h", "usr/include/5.1")
    pisitools.domove("/usr/include/lauxlib.h", "usr/include/5.1")
    pisitools.removeDir("/usr/include")

    pisitools.dohtml("doc")
    pisitools.newdoc("etc/README", "README.etc")
    pisitools.newdoc("test/README", "README.test")
    pisitools.dodoc("COPYRIGHT", "HISTORY", "README")
    pisitools.dodoc("README")