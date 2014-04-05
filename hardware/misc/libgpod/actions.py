#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--disable-static \
                         --disable-gtk-doc \
                         --without-hal \
                         --without-mono \
                         --with-temp-mount-dir=/run/libgpod \
                         --enable-udev \
                         --with-html-dir=/usr/share/doc/%s/html" % get.srcNAME())

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # For temporary mounts
    pisitools.dodir("/run/libgpod")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")
