#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -fPIC -fno-strict-aliasing" % get.CFLAGS())

def setup():
    autotools.aclocal("-I m4")
    autotools.autoheader()
    libtools.libtoolize()
    shelltools.system("intltoolize --force --copy --automake")
    autotools.autoreconf("-fi")
    autotools.configure("--with-openldap=yes \
                         --enable-smime=yes \
                         --program-prefix= --disable-dependency-tracking \
                         --disable-goa \
                         --enable-nss=yes \
                         --enable-dot-locking=no \
                         --enable-file-locking=fcntl \
                         --disable-maintainer-mode \
                         --enable-nntp=yes \
                         --enable-vala-bindings=yes \
                         --enable-introspection=yes \
                         --disable-weather \
                         --with-krb5=/usr \
                         --with-libdb=/usr ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "MAINTAINERS", "NEWS", "README", "TODO")
