#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-silent-rules \
                         --enable-keyring \
                         --enable-bash-completion \
                         --enable-archive \
                         --enable-afc \
                         --enable-bluray \
                         --enable-udev \
                         --disable-hal \
                         --enable-gphoto2 \
                         --enable-samba \
                         --enable-gtk=3 \
                         --enable-udisks2 \
                         --with-dbus-service-dir=/usr/share/dbus-1/services")

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.copy("daemon/trashlib/COPYING", "COPYING.GPL3")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
