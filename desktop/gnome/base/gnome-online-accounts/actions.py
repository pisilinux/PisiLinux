#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --enable-gtk-doc \
                         --enable-exchange \
                         --enable-facebook \
                         --enable-flickr \
                         --enable-google \
                         --enable-imap-smtp \
                         --enable-kerberos \
                         --enable-owncloud \
                         --enable-telepathy \
                         --enable-windows-live \
                         --libexec=/usr/lib/gnome-online-accounts")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "NEWS", "README")

