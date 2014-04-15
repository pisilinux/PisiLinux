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
    autotools.configure("\
                         --with-dbus-service-dir=/usr/share/dbus-1/services \
                         --disable-hal \
                         --disable-silent-rules \
                         --disable-static \
                         --enable-afc \
                         --enable-archive \
                         --enable-bash-completion \
                         --enable-bluray \
                         --enable-gphoto2 \
                         --enable-gtk=3 \
                         --enable-keyring \
                         --enable-samba \
                         --enable-udev \
                         --enable-udisks2 \
                        ")

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.copy("daemon/trashlib/COPYING", "COPYING.GPL3")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
