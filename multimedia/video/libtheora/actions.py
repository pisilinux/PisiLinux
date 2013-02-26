#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #disable doxygen for sandbox violations
    shelltools.export("ac_cv_prog_HAVE_DOXYGEN", "false")
    shelltools.export("ac_cv_prog_HAVE_PDFLATEX", "false")
    if get.buildTYPE() == "emul32":
        pisitools.dosed("configure.ac", "(.*OC_X86_64_ASM.*)", r"#\1")
        shelltools.system("./autogen.sh")
    autotools.configure("--enable-shared \
                         --enable-encode \
                         --disable-dependency-tracking \
                         --disable-spec \
                         --disable-sdltest \
                         --disable-examples \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s" docdir=/%s/libtheora' % (get.installDIR(), get.docDIR()))

    pisitools.dodoc("README", "AUTHORS", "CHANGES")
