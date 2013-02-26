#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())
    # autoheader fails when we "autoreconf -vif -Imacros" the package.
    #autotools.autoreconf("-vif -Imacros")
    autotools.aclocal("--force -Imacros")
    libtools.libtoolize("--copy --force")
    autotools.autoconf("--force -Imacros")

    autotools.configure("--with-readline \
                         --disable-sse2 \
                         --disable-rpath \
                         --disable-static \
                         --disable-openmp \
                         --enable-gui \
                         --without-gnome \
                         --with-gtksourceview \
                         --with-pic \
                         --with-audio \
                         --with-mpfr")

                         #Disable doc for now
                         # config.status: error: cannot find input file: `doc/commands/Makefile.in'
                         #--enable-build-doc \

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/applications", "gnome/gretl.desktop")
    pisitools.insinto("/usr/share/pixmaps", "gnome/gretl.png")
    pisitools.insinto("/usr/share/emacs/site-lisp", "utils/emacs/gretl.el")

    pisitools.doman("gretlcli.1")
    pisitools.removeDir("/usr/share/gretl/doc")

    pisitools.dodoc( "ChangeLog", "CompatLog", "COPYING", "README", "README.audio")
