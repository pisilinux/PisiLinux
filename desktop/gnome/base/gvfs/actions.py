#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static \
                         --enable-keyring \
                         --enable-bash-completion \
                         --enable-archive \
                         --enable-bluray \
                         --enable-udev \
                         --disable-hal \
                         --enable-gphoto2 \
                         --enable-samba \
                         --enable-gtk \
                         --enable-udisks2 \
                         --with-dbus-service-dir=/usr/share/dbus-1/services")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
