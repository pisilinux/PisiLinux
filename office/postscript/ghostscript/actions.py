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
    # Remove local copies for system libs
    for directory in ["cups/libs", "expat", "freetype", "jpeg", "lcms", "lcms2", "libpng", "openjpeg", "tiff", "zlib"]:
        shelltools.unlinkDir(directory)

    #pisitools.flags.add("-fno-strict-aliasing")

    autotools.autoreconf("-fi")

    options = "--disable-compile-inits \
               --disable-gtk \
               --enable-dynamic \
               --with-system-libtiff \
               --with-ijs \
               --with-drivers=ALL \
               --with-libpaper \
               --with-jbig2dec \
               --enable-fontconfig \
               --enable-freetype \
               --without-luratech \
               --with-system-libtiff \
               --without-omni \
               --with-x \
               --with-fontpath=/usr/share/fonts:/usr/share/fonts/default/ghostscript:/usr/share/cups/fonts:/usr/share/fonts/TTF:/usr/share/fonts/Type1:/usr/share/poppler/cMap/*"
    options += " --disable-cups --includedir=/usr/include --libdir=/usr/lib32" if get.buildTYPE() == "emul32" else " --enable-cups --with-install-cups"

    autotools.configure(options)

    shelltools.cd("ijs/")
    pisitools.dosed("configure.ac", "AM_PROG_CC_STDC", "AC_PROG_CC")
    shelltools.system("./autogen.sh \
                       --prefix=/usr \
                       --mandir=/usr/share/man \
                       --disable-static \
                       --enable-shared")

def build():
    autotools.make("-C ijs")
    autotools.make("so")
    autotools.make("-j1")
    if not get.buildTYPE() == "emul32": autotools.make("cups")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "soinstall")
    if not get.buildTYPE() == "emul32": autotools.rawInstall("-C ijs DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/*")
    pisitools.dodoc("doc/AUTHORS", "doc/COPYING")
