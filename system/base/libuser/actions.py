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

def setup():
    shelltools.export("AUTOPOINT", "true")

    autotools.autoreconf("-vfi")
    autotools.configure("--with-python \
                         --with-ldap \
                         --with-popt \
                         --disable-rpath \
                         --disable-gtk-doc-html")

def build():
    autotools.make()

    autotools.make("-C po update-gmo")

def install():
    autotools.rawInstall("DESTDIR='%s'" % get.installDIR())

    pisitools.dodoc("ABOUT*", "AUTHORS", "COPYING", "NEWS", "README")
