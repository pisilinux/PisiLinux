#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    #autotools.autoreconf("-vfi")
    autotools.configure("--with-svgz \
                         --with-croco \
                         --disable-gtk-doc \
                         --enable-pixbuf-loader \
                         --disable-static")
    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #for d in ["/usr/share/gtk-doc", "/usr/lib/gtk-3.0", "/usr/share/themes/bubble/gtk-3.0"]:
    #    pisitools.removeDir(d)

    pisitools.dodoc("COPYING", "AUTHORS", "ChangeLog", "README")
