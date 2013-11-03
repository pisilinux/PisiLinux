#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION())
WITHSSP = False
XTRA_FIXCFLAGS = "" if WITHSSP else "-fno-stack-protector" 
CFLAGS = "%s %s %s" % (get.CFLAGS(),
                       "-fomit-frame-pointer -fno-exceptions -fno-asynchronous-unwind-tables -Os -g3 -Werror-implicit-function-declaration -Wno-unused -Wno-switch",
                       XTRA_FIXCFLAGS)
MAKE_FLAGS = "CC=\"%s\" \
              CFLAGS=\"%s\" \
              PDIET=/usr/lib/dietlibc \
              STRIP=:" % (get.CC(), CFLAGS)

MAKE_TEST_FLAGS = "CC=\"%s\" \
                   CFLAGS=\"%s -fno-builtin\" \
                   PDIET=/usr/lib/dietlibc \
                   STRIP=:" % (get.CC(), CFLAGS)

def setup():
    shelltools.cd(get.workDIR())
    for f, l in [("dietlibc-github-c3f1cf67fcc186bb859e64a085bf98aaa6182a82.patch", 1),
                 ("dietlibc-0.33-biarch.patch", 0)]:
        shelltools.move(f, WorkDir)
        shelltools.cd(WorkDir)
        shelltools.system("patch --remove-empty-files --no-backup-if-mismatch -p%d -i %s" % (l, f))
        shelltools.cd("..")

    shelltools.cd(WorkDir)
    pisitools.dosed("Makefile", "^prefix\?=.*", "prefix=/usr/lib/dietlibc")
    pisitools.dosed("Makefile", "^(BINDIR=)[^\/]+(.*)", r"\1/usr\2")
    pisitools.dosed("Makefile", "^(MAN1DIR=)[^\/]+(.*)", r"\1/usr/share\2")
    pisitools.dosed("dietfeatures.h", "#define (WANT_LARGEFILE_BACKCOMPAT|WANT_VALGRIND_SUPPORT)", deleteLine=True)
    if not WITHSSP:
        pisitools.dosed("dietfeatures.h", "^(#define WANT_SSP)$", r"// \1")
        pisitools.dosed("dietfeatures.h", ".*(#define WANT_STACKGAP).*", r"\1")

def build():
    autotools.make("%s all" % MAKE_FLAGS)

    # Build tests
#    autotools.make("%s -C test all DIET=\"%s/bin-*/diet\" -k" % (MAKE_TEST_FLAGS, get.curDIR()))
#    autotools.make("%s -C test/inet all DIET=\"%s/bin-*/diet\"" % (MAKE_TEST_FLAGS, get.curDIR()))

#def check():
#    shelltools.cd("test")
#    shelltools.chmod("runtests-X.sh", 0755)
#    shelltools.system("ulimit -m $[ 128*1024 ] -v $[ 256*1024 ] -d $[ 128*1024 ] -s 512")
#    shelltools.system("./runtests-X.sh")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Simple wrapper for gcc
    host_gcc = "/usr/bin/%s-dietlibc-gcc" % get.HOST()
    shelltools.echo("%s%s" % (get.installDIR(), host_gcc), """\
#!/bin/bash
exec /usr/bin/diet %s "$@"
""" % get.CC())

    shelltools.chmod("%s%s" % (get.installDIR(), host_gcc), 0755)
    pisitools.dosym(host_gcc, "/usr/bin/dietlibc-gcc")

    pisitools.dodoc("AUTHOR", "BUGS", "CAVEAT", "CHANGES", "FAQ", "README*", "THANKS", "TODO")
