#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.flags.add("-flto -ffat-lto-objects")
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
	                     --enable-xlib \
                         --enable-ft \
	                     --enable-ps \
                         --enable-pdf \
	                     --enable-svg \
	                     --enable-tee \
	                     --enable-gl \
	                     --enable-gobject \
	                     --disable-gtk-doc")

    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.dodoc("AUTHORS", "README", "ChangeLog", "NEWS", "COPYING", "COPYING-LGPL-2.1", "COPYING-MPL-1.1")
