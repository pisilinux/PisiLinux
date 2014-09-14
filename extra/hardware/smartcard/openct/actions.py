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
    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE" % get.CFLAGS())
    autotools.configure("--disable-static \
                         --enable-usb \
                         --enable-doc \
                         --enable-pcsc \
                         --with-bundle=/usr/lib/pcsc/drivers \
                         --with-udev=/lib/udev")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    pisitools.dodir("/lib/udev/rules.d")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # udev support
    pisitools.insinto("/lib/udev/rules.d/", "etc/openct.udev", "95-openct.rules")

    pisitools.dodir("/run/openct")
    shelltools.chmod("%s/run/openct" % get.installDIR(), 0755)

    pisitools.remove("/usr/lib/openct-ifd.so")

    pisitools.dodoc("NEWS", "TODO", "doc/README")
