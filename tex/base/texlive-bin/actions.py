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
                         --disable-dump-share \
                         --disable-aleph \
                         --disable-static \
                         --disable-xindy-rules \
                         --disable-dependency-tracking \
                         --disable-mktexmf-default \
                         --disable-web2c \
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
    autotools.rawInstall("prefix=/usr DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/tlpkg/TeXLive")
    shelltools.move("%s/source/utils/biber/TeXLive/*.pm" % get.workDIR(), "%s/usr/share/tlpkg/TeXLive" % get.installDIR())
    
    #pisitools.remove("/usr/bin/biber")
    #shelltools.move("%s/biber" % get.workDIR(), "%s/usr/bin/" % get.installDIR())
    #pisitools.insinto("/usr/bin/", "%s/biber" % get.workDIR())