#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    options = "--disable-static \
               --disable-silent-rules \
               --enable-introspection \
               --with-libjasper \
               --with-x11 \
               --with-included-loaders=png \
              "
    if get.buildTYPE() == "emul32":
        options += " --bindir=/_emul32/bin \
                   "

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32":
        pisitools.domove("/_emul32/bin/gdk-pixbuf-query-loaders", "/usr/bin", "gdk-pixbuf-query-loaders-32")
        pisitools.removeDir("/_emul32")
        return

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
