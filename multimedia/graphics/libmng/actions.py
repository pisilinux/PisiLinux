#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.sym("makefiles/configure.in", "configure.in")
    shelltools.sym("makefiles/Makefile.am", "Makefile.am")
    shelltools.sym("makefiles/makefile.linux", "Makefile")
    #shelltools.sym("contrib/gcc/sdl-mngplay/acinclude.m4", "acinclude.m4")
    
    shelltools.system("sed -i -e 's/unroll-loops/& -fPIC/' Makefile ")

    autotools.autoreconf("-fiv")
    autotools.configure("--with-jpeg \
                         --with-lcms \
                         --disable-static \
                         --disable-dependency-tracking")

    if get.buildTYPE() == "emul32":
        options = " --libdir=/usr/lib32 \
                    --with-jpeg \
                    --disable-static \
                    --disable-dependency-tracking"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.doman("doc/man/*")
    pisitools.dodoc("CHANGES", "LICENSE", "README*", "doc/doc.readme", "doc/misc/*", "doc/libmng.txt")
