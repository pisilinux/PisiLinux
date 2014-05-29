#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import texlivemodules

import os

WorkDir = "."

def setup():
    
    shelltools.makedirs("%s/source/build" % get.workDIR())
    shelltools.cd("%s/source/build" % get.workDIR())
    shelltools.sym("../configure", "configure")
    autotools.configure("--disable-native-texlive-build \
                         --disable-multiplatform \
                         --disable-chktex \
                         --disable-dialog \
                         --disable-detex \
                         --disable-dvipng \
                         --disable-dvi2tty \
                         --disable-dvipdfmx \
                         --disable-lcdf-typetools \
                         --disable-ps2eps \
                         --disable-psutils \
                         --disable-t1utils \
                         --disable-bibtexu \
                         --disable-xz \
                         --disable-xdvik \
                         --disable-dump-share \
                         --disable-aleph \
                         --disable-static \
                         --disable-web2c \
                         --disable-xindy-rules \
                         --disable-dependency-tracking \
                         --disable-mktexmf-default \
                         --disable-xindy-rules \
                         --enable-xindy-docs \
                         --enable-shared \
                         --enable-build-in-source-tree \
                         --enable-xindy \
                         --with-system-zlib \
                         --with-system-zziplib \
                         --with-system-pnglib \
                         --with-system-ncurses \
                         --with-system-t1lib \
                         --with-system-gd \
                         --with-system-poppler \
                         --with-system-xpdf \
                         --with-system-freetype2 \
                         --with-system-pixman \
                         --with-system-icu \
                         --with-system-graphite2 \
                         --with-system-cairo \
                         --with-system-harfbuzz \
                         --with-freetype2-libdir=/usr/lib \
                         --with-freetype2-include=/usr/include/freetype2 \
                         --with-xdvi-x-toolkit=xaw \
                         --with-banner-add=/PisiLinux \
                         --with-clisp-runtime=default ")


def build():
  
    shelltools.cd("%s/source/build/" % get.workDIR())
    autotools.make()
 
def install():
  
    shelltools.cd("%s/source/build/" % get.workDIR())
    autotools.install("prefix=%s/source/build/usr" % get.workDIR())

    pisitools.dodir("/usr/share/tlpkg/TeXLive")

    shelltools.move("%s/source/build/usr/bin" % get.workDIR(), "%s/usr" % get.installDIR()) 
    shelltools.move("%s/source/build/usr/lib" % get.workDIR(), "%s/usr" % get.installDIR())
    shelltools.move("%s/source/build/usr/include" % get.workDIR(), "%s/usr" % get.installDIR())
    shelltools.move("%s/source/build/usr/share/texmf-dist" % get.workDIR(), "%s/usr/share" % get.installDIR())
    shelltools.move("%s/source/utils/biber/TeXLive/*.pm" % get.workDIR(), "%s/usr/share/tlpkg/TeXLive" % get.installDIR())


    #pisitools.insinto("/usr/bin/", "%s/biber" % get.workDIR())