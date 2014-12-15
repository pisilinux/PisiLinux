#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/Makefile", "^CFLAGS.*$", "CFLAGS=%s -fPIC -DLUA_USE_LINUX" % get.CFLAGS())
    pisitools.dosed("src/Makefile", "^MYLDFLAGS.*$", "MYLDFLAGS=%s" % get.LDFLAGS())

def build():
    autotools.make("linux")

def install():
    autotools.rawInstall("INSTALL_TOP=%s/usr" % get.installDIR())

    pisitools.dosym("/usr/lib/liblua.so.5.1", "/usr/lib/liblua.so")

    #pisitools.insinto("/usr/share/lua/5.1", "etc/strict.lua")
    #pisitools.insinto("/usr/share/lua/5.1", "test/*.lua")
    #pisitools.insinto("/usr/lib/pkgconfig", "etc/lua.pc")

    pisitools.dohtml("doc")
    #pisitools.newdoc("etc/README", "README.etc")
    #pisitools.newdoc("test/README", "README.test")
    pisitools.dodoc("README")
