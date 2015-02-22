#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

iscan_data = "iscan-data-1.35.0"

def setup():
    # Setup iscan-data
    shelltools.cd(iscan_data)
    autotools.configure()
    shelltools.cd("..")

    shelltools.unlink("m4/libtool.m4")

    shelltools.export("AUTOPOINT", "true")
    shelltools.export("LDFLAGS", "-ldl -lpng16")
    autotools.autoreconf("-vif")

    autotools.configure("--disable-static \
                         --enable-frontend \
                         --enable-gimp=no \
                         --enable-jpeg \
                         --enable-tiff \
                         --enable-png \
                         --enable-dependency-reduction \
                         --disable-rpath")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-C %s" % iscan_data)
    autotools.make()
    autotools.make("-C po update-po")

def install():
    autotools.install()
    autotools.install("-C %s" % iscan_data)

    # Remove unused stuff from iscan-data
    #pisitools.remove("/usr/share/iscan-data/sled10*")
    #pisitools.remove("/usr/share/iscan-data/fdi.xsl")

    # Install sane backend configuration file
    pisitools.insinto("/etc/sane.d", "backend/epkowa.conf")

    # Install documentation
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

    # Needed for iscan-registry
    pisitools.dodir("/var/lib/iscan")
