#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #autotools.autoreconf("-fi")
    autotools.configure("--with-distro=none \
                         --disable-monodoc \
                         --disable-static \
                         --disable-xmltoman \
                         --disable-qt3 \
                         --enable-qt4 \
                         --disable-python \
                         --disable-doxygen-doc \
                         --disable-glib \
                         --disable-gobject \
                         --disable-gtk \
                         --disable-gtk3 \
                         --disable-introspection \
                         --disable-mono \
                         --disable-compat-howl \
                         --disable-compat-libdns_sd \
                         --with-systemdsystemunitdir=no \
                         --with-avahi-user=avahi \
                         --with-avahi-group=avahi \
                         --with-autoipd-user=avahi-autoipd \
                         --with-autoipd-group=avahi-autoipd \
                         --with-avahi-priv-access-group=avahi")

def build():
    autotools.make("-C avahi-common")
    autotools.make("-C avahi-qt")
    autotools.make("all-am")

def install():
    autotools.rawInstall("-C avahi-qt DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/lib/pkgconfig", "avahi-qt4.pc")
