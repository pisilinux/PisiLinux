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
    autotools.autoreconf("-fiv")

    autotools.configure("\
                         --enable-mime \
                         --enable-extras \
                         --enable-contrast \
                         --with-lensfun \
                         --with-exiv2 \
                         --with-libexif \
                        ")

    pisitools.dosed("Makefile", "/usr/lib/gimp/", "%s/usr/lib/gimp/" % get.installDIR())

def build():
    autotools.make("schemasdir=/etc/gconf/schemas")

def install():
    autotools.install("schemasdir=%s/etc/gconf/schemas" % get.installDIR())

    # Do not conflict with dcraw package
    pisitools.remove("/usr/bin/dcraw")

    pisitools.insinto("/usr/share/mime/packages", "ufraw-mime.xml")

    pisitools.dodoc("COPYING", "MANIFEST", "README")
