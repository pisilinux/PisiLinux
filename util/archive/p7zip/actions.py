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

WorkDir = "p7zip_%s" % get.srcVERSION()

makefiles = {
             'i686'     : "makefile.linux_x86_asm_gcc_4.X",
             'x86_64'   : "makefile.linux_amd64_asm"
            }

def setup():
    shelltools.copy(makefiles[get.ARCH()], "makefile.machine")

    for i in shelltools.ls("makefile.*"):
        pisitools.dosed(i, "^CC=gcc ", "CC=%s " % get.CC())
        pisitools.dosed(i, "^CXX=g\+\+ ", "CXX=%s " % get.CXX())

def build():
    # do not force CC and CXX here since asm build fails
    autotools.make('OPTFLAGS="%s -DHAVE_GCCVISIBILITYPATCH -fvisibility=hidden -fvisibility-inlines-hidden" \
                    all3' % get.CFLAGS())

def install():
    pisitools.insinto("/usr/lib/p7zip","bin/*")

    # p7zip wrapper
    pisitools.dobin("contrib/gzip-like_CLI_wrapper_for_7z/p7zip")
    pisitools.doman("contrib/gzip-like_CLI_wrapper_for_7z/man1/p7zip.1")

    pisitools.dohtml("DOCS/MANUAL/*")
    pisitools.dodoc("ChangeLog", "README", "TODO", "DOCS/*.txt")
