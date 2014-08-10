#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.flags.add("-Wno-unused-but-set-variable")
    autotools.autoreconf()
    autotools.autoconf()

    autotools.configure("--disable-static \
                         --disable-gcc-warnings")
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")


def build():
    autotools.make("V=1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
    pisitools.dodoc("doc/API", "doc/USER.jp", "doc/FAT")

