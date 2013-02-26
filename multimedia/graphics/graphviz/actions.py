#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

def setup():
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
