#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.system("sed -r -e '/^LUA_(SO|A|T)=/ s/lua/lua5.1/' -e '/^LUAC_T=/ s/luac/luac5.1/' \
    -i src/Makefile")
    pisitools.dosed("src/Makefile", "^CFLAGS.*$", "CFLAGS=%s -DLUA_USE_LINUX" % get.CFLAGS())
    pisitools.dosed("src/Makefile", "^MYLDFLAGS.*$", "MYLDFLAGS=%s" % get.LDFLAGS())
    autotools.make("linux")

def install():
    options = "TO_BIN=\"lua5.1 luac5.1\" \
               TO_LIB=\"liblua5.1.a liblua5.1.so liblua5.1.so.5.1 liblua5.1.so.5.1.5 \" \
               INSTALL_DATA=\"cp -d\" \
               INSTALL_TOP=\"%s/usr\"  \
               INSTALL_INC=\"%s/usr/include/lua5.1\" \
               INSTALL_MAN=%s/usr/share/man/man1" % (get.installDIR(),get.installDIR(),get.installDIR())
    autotools.rawInstall(options)

    pisitools.removeDir("/usr/share/lua")
    pisitools.removeDir("/usr/lib/lua")
    
    pisitools.dosym("/usr/lib/liblua5.1.so", "/usr/lib/liblua.so.5.1")

    docs = [ "*.html", "*.png", "*.css", "*.gif" ]
    for d in docs:
        pisitools.insinto("/usr/share/doc/lua", "doc/%s" % d)
    pisitools.rename("/usr/share/man/man1/lua.1", "lua.5.1.1")
    pisitools.rename("/usr/share/man/man1/luac.1", "luac.5.1.1")
