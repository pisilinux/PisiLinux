#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

CFLAGS = "%s %s" % (get.CFLAGS(), "-Os -fno-exceptions -fno-asynchronous-unwind-tables -fno-stack-protector -Werror-implicit-function-declaration")
MAKE_FLAGS = "CC=\"%s\" \
              CFLAGS=\"%s\" \
              PDIET=/usr/lib/dietlibc" % (get.CC(), CFLAGS)

def build():
    autotools.make("%s -j1 all" % MAKE_FLAGS)

    # Build tests
    autotools.make("%s -C test all DIET=\"%s/bin-*/diet\" -k" % (MAKE_FLAGS, get.curDIR()))
    autotools.make("%s -C test/inet all DIET=\"%s/bin-*/diet\"" % (MAKE_FLAGS, get.curDIR()))

    # Symlink all to the fedora wrapper test script
    for t in ("test", "test/stdio", "test/inet", "test/stdlib", "test/dirent", "test/string", "test/time"):
        shelltools.sym("%s/runtests-X.sh" % get.curDIR(), "%s/%s/runtests-X.sh" % (get.curDIR(), t))

#def check():
    #shelltools.chmod("%s/runtests-X.sh" % get.curDIR(), 0755)
    #shelltools.cd("test")
    #shelltools.system("./runtests-X.sh")

def install():
    autotools.rawInstall("-j1 %s DESTDIR=%s" % (MAKE_FLAGS, get.installDIR()))

    # Simple wrapper for gcc
    host_gcc = "/usr/bin/%s-dietlibc-gcc" % get.HOST()
    shelltools.echo("%s%s" % (get.installDIR(), host_gcc), """\
#!/bin/bash
exec /usr/bin/diet %s "$@"
""" % get.CC())

    shelltools.chmod("%s%s" % (get.installDIR(), host_gcc), 0755)
    pisitools.dosym(host_gcc, "/usr/bin/dietlibc-gcc")

    pisitools.dodoc("AUTHOR", "BUGS", "CAVEAT", "CHANGES", "FAQ", "README", "THANKS", "TODO")
