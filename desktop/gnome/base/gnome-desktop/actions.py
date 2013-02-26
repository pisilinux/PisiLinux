#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-scrollkeeper \
                         --enable-gtk-doc \
                         --with-gnome-distributor=\"Pardus\" \
                         --with-pnp-ids-path=%s/misc/pnp.ids" % get.dataDIR())

def build():
    autotools.make("LIBS=-lm")

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "Change*", "HACKING", "MAINTAINERS", "NEWS", "README")
