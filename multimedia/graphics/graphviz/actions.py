#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

def setup():
    # install the graph and cgraph api alongside
    pisitools.dosed("lib/graph/Makefile.in", "@WITH_CGRAPH_FALSE@", "")

    #autotools.autoreconf("-vfi")

    #R support is disabled because of its deps.
    autotools.configure("--disable-static \
                         --with-libgd \
                         --with-pangocairo \
                         --with-fontconfig \
                         --with-devil=no \
                         --disable-dependency-tracking \
                         --disable-php \
                         --disable-r \
                         --disable-lua \
                         --disable-ocaml \
                         --disable-sharp \
                         --disable-io \
                         --disable-rpath")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #remove empty directories
    #for lang in ["lua", "ocaml", "php", "python23", "python24", "python25", "R", "sharp"]:
        #pisitools.removeDir("/usr/lib/graphviz/%s" % lang)

    pisitools.domove("usr/lib64/tcl8.6", "/usr/lib")
    pisitools.removeDir("usr/lib64")

    pisitools.dohtml(".")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*")

    pisitools.removeDir("/usr/share/graphviz/doc")

    # everything has been built against cgraph, but use graph as default api
    pisitools.dosed("%s/usr/include/graphviz/types.h" % get.installDIR(), r"#define WITH_CGRAPH 1", deleteLine=True)
