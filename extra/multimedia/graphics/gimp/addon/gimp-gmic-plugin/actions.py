#!/usr/bin/python
# -*- actions.pycoding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#def setup():

def build():
    #pisitools.dosed("src/Makefile", "^(FFMPEG_LDFLAGS\s=.*)", r"\1 -lavutil")
    autotools.make("-C src gimp custom lib -j1")

def install():
    pisitools.doman("man/gmic.1.gz")
    pisitools.dodoc("COPYING", "README")
    pisitools.insinto("/usr/share/doc/gimp-gmic-plugin", "COPYING")
    pisitools.insinto("/etc/bash_completion.d/", "resources/gmic_bashcompletion.sh", destinationFile = "gmic")
    shelltools.cd("src")
    pisitools.dobin("gmic")
    pisitools.doexe("gmic_gimp", "/usr/lib/gimp/2.0/plug-ins/")
    pisitools.insinto("/usr/include", "gmic.h")    
    pisitools.dolib("libgmic.so")
    ver = ".%s" % get.srcVERSION()
    while ver:
        pisitools.dosym("libgmic.so", "/usr/lib/libgmic.so%s" % ver)
        ver = ver[:ver.rfind('.')]
