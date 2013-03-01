#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    shelltools.cd("src")

    autotools.autoreconf("-fi")
    autotools.configure("--with-usbids-dir=/usr/share/misc \
                         --disable-static \
                         --disable-usbids-install")

def build():
    autotools.make("-C src")

def install():
    autotools.rawInstall("-C src DESTDIR=%s install-data" % get.installDIR())

    pisitools.removeDir("/usr/share/usbip")

    pisitools.dodoc("COPYING", "src/README")
