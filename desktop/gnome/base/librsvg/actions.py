#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #for d in ["/usr/share/gtk-doc", "/usr/lib/gtk-3.0", "/usr/share/themes/bubble/gtk-3.0"]:
    #    pisitools.removeDir(d)

    pisitools.dodoc("COPYING", "AUTHORS", "ChangeLog", "README")
