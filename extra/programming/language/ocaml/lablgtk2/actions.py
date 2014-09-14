#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "lablgtk-%s" % get.srcVERSION()

def setup():
    shelltools.export("CFLAGS", get.CFLAGS())
    shelltools.export("CXXFLAGS", get.CXXFLAGS())

    autotools.autoreconf("-vif")
    autotools.configure("--with-glade \
                         --with-gl \
                         --with-rsvg \
                         --with-gnomecanvas \
                         --with-gnomeui \
                         --with-gtkspell \
                         --without-gtksourceview \
                         --without-gtksourceview2 \
                         --without-quartz \
                         --without-panel")

def build():
    autotools.make("-j1 world")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib/ocaml/lablgtk2/*.a")

    pisitools.dodoc("CHANGES*", "COPYING", "LGPL", "README*")
    pisitools.insinto("%s/lablgtk2" % get.docDIR(), "examples")
