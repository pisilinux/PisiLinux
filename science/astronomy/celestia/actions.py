#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

def setup():
    pisitools.flags.add("-fsigned-char")
    pisitools.dosed("configure.in", "AM_CONFIG_HEADER", "AC_CONFIG_HEADERS")
    autotools.autoreconf("-fi")
    autotools.configure("--with-gtk \
                         --with-pic \
                         --with-qt \
                         --enable-pch \
                         --disable-rpath \
                         --enable-theora \
                         --enable-cairo \
                         --without-arts \
                         --with-lua")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s MKDIR_P='mkdir -p'" % get.installDIR())
    
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "COPYING", "README", "TRANSLATORS", "locale/COPYING_*")