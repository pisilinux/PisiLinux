#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "motif-2.3.4"

mwmlibdir = "/usr/lib/X11"
mwmconfigdir = "/etc/X11/mwm"

def setup():
    # add X.Org vendor string to aliases for virtual bindings
    shelltools.echo("bindings/xmbind.alias", '"The X.Org Foundation"\t\t\t\t\tpc')

    # libXp will be deprecated
    pisitools.dosed("lib/Xm/Makefile.am", " -lXp ", " -ldeprecatedXp ")

    shelltools.export("LANG", "C") # guess why this is here...
    shelltools.export("LC_ALL", "C") # guess why this is here...
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -fno-strict-aliasing" % get.CXXFLAGS())
    shelltools.export("AT_M4DIR", ".")

    for f in ["NEWS", "AUTHORS"]:
        shelltools.touch(f)

    autotools.autoreconf("-vfi")


    options = "--with-x \
              --disable-static \
              --enable-utf8 \
              --enable-xft \
              --enable-jpeg \
              --enable-png"

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32 \
                     --bindir=/emul32/bin \
                     --mandir=/emul32/man"

        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        shelltools.export("CFLAGS", "%s -I/usr/include/freetype2 -fno-strict-aliasing -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -I/usr/include/freetype2 -fno-strict-aliasing -m32" % get.CXXFLAGS())
        shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())

    autotools.configure(options)


def build():
    autotools.make('-j1 MWMRCDIR="/etc/X11/mwm"')

def install():
    autotools.rawInstall('DESTDIR=%s -j1 MWMRCDIR="/etc/X11/mwm"' % get.installDIR())

    # these are just demos
    if not get.buildTYPE() == "emul32":
        pisitools.removeDir("/usr/share/Xm")

    pisitools.dodoc("ChangeLog", "README*", "BUGREPORT", "RELEASE", "RELNOTES", "TODO")

    #if get.buildTYPE() == "emul32":
        #pisitools.removeDir("/emul32")

