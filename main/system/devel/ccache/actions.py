#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    if shelltools.isDirectory("zlib"):
        shelltools.unlinkDir("zlib")

    autotools.configure("--prefix=/usr")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

    # Create symlinks
    for cc in ("gcc", "g++", "cc", "c++"): # , "clang" , "clang++"
        pisitools.dosym("../../../bin/ccache", "/usr/lib/ccache/bin/%s" % cc)
        #pisitools.dosym("../../../bin/ccache", "/usr/lib/ccache/bin/%s-%s" % (get.HOST(), cc))

    #pisitools.dodoc("LICENSE.txt", "README.txt")
