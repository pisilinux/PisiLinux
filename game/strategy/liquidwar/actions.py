#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "liquidwar6-0.0.10beta"
#WorkDir = "liquidwar6-%ssnapshot" % get.srcVERSION().split("_", 1)[1]

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --enable-mod-ogg \
                         --enable-mod-gl \
                         --disable-nls \
                         --disable-rpath")

    # pisitools.dosed("Makefile", "^DOCDIR.*", "DOCDIR = /%s/%s" % (get.docDIR(), get.srcNAME()))

def build():
    # autotools.make("-j1")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # autotools.make("DESTDIR=%s install_nolink" % get.installDIR())
    # pisitools.removeDir("/usr/share/applnk")
