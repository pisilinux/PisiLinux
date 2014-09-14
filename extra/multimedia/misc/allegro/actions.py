#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DDOCDIR=share/doc \
                          -DINFODIR=share/info \
                          -DMANDIR=share/man \
                          -DWANT_ALSA=ON \
                          -DWANT_EXAMPLES=OFF \
                          -DWANT_JACK=OFF \
                          -DWANT_JPEGALLEG=ON \
                          -DWANT_LINUX_CONSOLE=OFF \
                          -DWANT_LINUX_FBCON=ON \
                          -DWANT_LINUX_SVGALIB=ON \
                          -DWANT_LINUX_VGA=ON \
                          -DWANT_LOADPNG=ON \
                          -DWANT_LOGG=ON \
                          -DWANT_OSS=ON \
                          -DWANT_TESTS=OFF \
                          -DWANT_X11=ON \
                          -DWANT_ALLEGROGL=ON \
                          ")

def build():
    cmaketools.make()

def install():
    cmaketools.install('DESTDIR="%s"' % get.installDIR())
    pisitools.dohtml("docs/html/*")

