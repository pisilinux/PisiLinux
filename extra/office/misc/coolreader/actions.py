#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("cr3qt/CMakeLists.txt", "share/cr3", "share/coolreader")
    cmaketools.configure("-DGUI=QT \
-DCMAKE_BUILD_TYPE=Release \
-DMAX_IMAGE_SCALE_MUL=2 \
-DDOC_DATA_COMPRESSION_LEVEL=3 \
-DDOC_BUFFER_SIZE=0x1400000", installPrefix="/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("changelog", "README.TXT")
    pisitools.removeDir("/usr/share/doc/cr3")
