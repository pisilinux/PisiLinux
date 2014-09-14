#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-scrollkeeper \
                         --enable-gtk-doc \
                         --with-gnome-distributor=\"PisiLinux\" \
                         --with-pnp-ids-path=%s/misc/pnp.ids" % get.dataDIR())
    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make("LIBS=-lm")

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "Change*", "HACKING", "MAINTAINERS", "NEWS", "README")
