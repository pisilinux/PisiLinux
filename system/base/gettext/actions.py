#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

docdir = "/%s/%s" % (get.docDIR(), get.srcNAME())

shelltools.export("LC_ALL", "C")

def setup():
    # shelltools.export("CFLAGS","%s -Dgcc_is_lint" % get.CFLAGS())
    # shelltools.export("CXXFLAGS","%s -Dgcc_is_lint" % get.CXXFLAGS())

    # Build with --without-included-gettext (will use that of glibc), as we
    # need preloadable_libintl.so for new help2man

    # autoreconf breaks linker, graaaaaaaaggggghhhhhhh
    # autotools.autoreconf("-vfi")
    autotools.configure("--disable-java \
                         --disable-native-java \
                         --disable-csharp \
                         --without-included-gettext \
                         --with-included-libcroco \
                         --with-included-glib \
                         --with-included-libxml \
                         --with-pic=yes \
                         --without-emacs \
                         --disable-openmp \
                         --enable-nls \
                         --enable-shared \
                         --disable-git \
                         --disable-rpath \
                         --disable-static")

def build():
    autotools.make("GMSGFMT=../src/msgfmt")

def install():
    autotools.rawInstall("DESTDIR=%s docdir=/%s/html" % (get.installDIR(), docdir))

    pisitools.doexe("gettext-tools/misc/gettextize", "/usr/bin")

    # Remove C# & Java stuff
    pisitools.remove("%s/html/examples/build-aux/csharp*" % docdir)
    pisitools.remove("%s/html/examples/build-aux/java*" % docdir)
    pisitools.removeDir("%s/html/examples/*java*" % docdir)
    pisitools.removeDir("%s/html/*java*" % docdir)

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog*", "HACKING", "NEWS", "README*", "THANKS")

