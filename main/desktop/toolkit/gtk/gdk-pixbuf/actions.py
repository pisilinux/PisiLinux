#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    options = "\
                 --disable-static \
                 --disable-silent-rules \
                 --with-libjasper \
                 --with-x11 \
                 --with-included-loaders=png \
              "

    options += "\
                 --bindir=/_emul32/bin \
                 --disable-introspection \
               " if get.buildTYPE() == "emul32" else \
               "\
                 --enable-introspection \
               "
    autotools.configure(options)

    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32":
        pisitools.domove("/_emul32/bin/gdk-pixbuf-query-loaders", "/usr/bin", "gdk-pixbuf-query-loaders-32")
        pisitools.removeDir("/_emul32")
        return
    pisitools.dosym("/usr/bin/gdk-pixbuf-query-loaders", "/usr/bin/gdk-pixbuf-query-loaders-64")
    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
