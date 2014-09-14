#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #https://projects.archlinux.org/svntogit/packages.git/plain/trunk/rl63.patch?h=packages/seed
    pisitools.dosed("modules/readline/seed-readline.c", "Function *", "rl_command_func_t *")
    autotools.configure("--disable-static \
                         --with-webkit=3.0 \
                         --enable-readline-module \
                         --enable-os-module \
                         --enable-ffi-module \
                         --enable-gtkbuilder-module \
                         --enable-cairo-module \
                         --enable-gettext-module \
                         --enable-dbus-module \
                         --enable-mpfr-module \
                         --enable-sqlite-module \
                         --enable-libxml-module")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "NEWS", "README")

