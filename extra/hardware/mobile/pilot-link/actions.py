#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")

    autotools.configure("--disable-debug \
                         --enable-static=no \
                         --includedir=/usr/include/libpisock \
                         --with-java=no \
                         --with-tcl=no \
                         --with-perl=yes \
                         --with-python=yes \
                         --with-libpng=/usr \
                         --with-readline=yes \
                         --with-bluez \
                         --enable-conduits \
                         --enable-threads \
                         --enable-libusb")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    perlmodules.removePodfiles()

    shelltools.copy("%s/usr/share/%s/udev*" % (get.installDIR(), get.srcNAME()), "%s/etc/udev/rules.d/" % get.installDIR())

    pisitools.dodoc("ChangeLog", "README", "doc/README*", "doc/TODO", "NEWS", "AUTHORS")
