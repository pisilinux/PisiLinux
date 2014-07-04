#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

major, minor = get.srcVERSION().split(".", 1)

def setup():
    shelltools.system("setconf Makefile TINYXML_USE_STL YES")
    shelltools.system('setconf Makefile RELEASE_CFLAGS "$CXXFLAGS -fPIC"')
    #pisitools.dosed("Makefile", "@MAJOR_V@", "%s" % major)
    #pisitools.dosed("Makefile", "@MINOR_V@", "%s" % minor)

def build():
    autotools.make()
    shelltools.system('g++ -fPIC "$CXXFLAGS" -shared -o "libtinyxml.so.0.2.6.2" \
      -Wl,-soname,"libtinyxml.so.0" $(ls *.o | grep -v xmltest)')

def install():
    pisitools.insinto("/usr/include", "*.h")
    # pisi dolib does not care for symlinks
    # pisitools.dolib("libtinyxml.so*")
    for i in shelltools.ls("libtinyxml.so*"):
        pisitools.insinto("/usr/lib/", i)
    
    pisitools.dosym("/usr/lib/libtinyxml.so.0.2.6.2", "usr/lib/libtinyxml.so.0")
    pisitools.dosym("/usr/lib/libtinyxml.so.0.2.6.2", "usr/lib/libtinyxml.so")
    pisitools.dodoc("changes.txt", "readme.txt")
    pisitools.dohtml("docs/*")
