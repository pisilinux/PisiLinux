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
    options = "--disable-static \
               --disable-silent-rules \
               --disable-gtk-doc \
               --enable-xlib \
               --enable-xlib-xrender \
               --enable-xcb \
               --enable-ft \
               --enable-gl \
               --enable-pdf \
               --enable-ps \
               --enable-svg \
               --enable-tee \
               --enable-png \
               --disable-xlib-xcb \
               --with-x"
    if get.buildTYPE() == "emul32":
        options += "\
                    --disable-pdf \
                    --disable-ps \
                    --disable-svg \
                   "
    autotools.autoreconf("-vfi")
    autotools.configure(options)
    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.dodoc("AUTHORS", "README", "ChangeLog", "NEWS", "COPYING", "COPYING-LGPL-2.1", "COPYING-MPL-1.1")
