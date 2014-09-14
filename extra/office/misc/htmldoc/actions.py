#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-rpath \
                         --disable-localpng \
                         --disable-localjpeg \
                         --disable-localzlib \
                         --with-openssl-libs \
                         --with-openssl-includes")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/*.html")
    pisitools.dohtml("doc/*.png")

    pisitools.insinto("/usr/share/applications", "desktop/htmldoc.desktop")
    pisitools.insinto("/usr/share/icons/", "desktop/htmldoc-48.png")
