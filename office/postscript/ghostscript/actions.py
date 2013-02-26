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
    # Remove local copies for system libs
    for directory in ["expat", "freetype", "jasper", "jpeg", "lcms", "lcms2", "libpng", "openjpeg", "tiff", "zlib"]:
        shelltools.unlinkDir(directory)

    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())

    autotools.autoreconf("-fi")
    
    options = "--disable-compile-inits \
               --disable-gtk \
               --enable-dynamic \
               --with-system-libtiff \
               --with-ijs \
               --with-drivers=ALL \
               --with-libpaper \
               --with-jbig2dec \
               --with-jasper \
               --enable-fontconfig \
               --enable-freetype \
               --without-luratech \
               --with-system-libtiff \
               --with-omni \
               --with-x \
               --with-fontpath=/usr/share/fonts:/usr/share/fonts/default/ghostscript:/usr/share/cups/fonts:/usr/share/fonts/TTF:/usr/share/fonts/Type1:/usr/share/poppler/cMap/*"
    options += " --disable-cups" if get.buildTYPE() == "emul32" else " --enable-cups"

    autotools.configure(options)

    shelltools.cd("ijs/")
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

    # For cjk stuff
    #pisitools.dodir("/usr/share/ghostscript/Resource/Init")

    # Install missing header
    #pisitools.insinto("/usr/include/ghostscript", "base/errors.h")

    # Install ijs
    autotools.rawInstall("-C ijs DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/lib/pkgconfig")

    # Remove ijs examples
    pisitools.remove("/usr/bin/ijs_*_example")
    pisitools.remove("/usr/lib/libijs-0.35.so")
    pisitools.remove("/usr/share/man/man1/ijs-config.1")
    pisitools.remove("/usr/lib/libijs.so")
    pisitools.remove("/usr/include/ijs/ijs_client.h")
    pisitools.remove("/usr/bin/ijs-config")
    pisitools.remove("/usr/include/ijs/ijs_server.h")
    pisitools.remove("/usr/include/ijs/ijs.h")

    # Install docs
    #pisitools.remove("/usr/share/doc/ghostscript/*.htm*")
    #pisitools.remove("/usr/share/doc/ghostscript/*.css")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("doc/AUTHORS", "doc/COPYING")
