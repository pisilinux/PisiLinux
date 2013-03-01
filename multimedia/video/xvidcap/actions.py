#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    shelltools.system("intltoolize --copy --force")
    shelltools.export("PTHREAD_LIBS", "-lpthread")  

    autotools.configure("--without-forced-embedded-ffmpeg \
                         --with-x \
                         --with-gtk2 \
                         --enable-libtheora \
                         --disable-dependency-tracking \
                         --without-forced-embedded-ffmpeg \
                         --enable-libmp3lame")

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/bin", "src/xvidcap")
    pisitools.insinto("/usr/bin", "src/xvidcap-dbus-client")
    pisitools.insinto("/usr/share/applications/xvidcap/", "xvidcap.desktop")
    pisitools.insinto("/usr/share/pixmaps/", "xvidcap.png")
    pisitools.insinto("/usr/share/xvidcap/help/C/figures", "doc/xvidcap/C/figures/*.png")
    pisitools.insinto("/usr/share/xvidcap/help/C/figures", "doc/xvidcap/C/*.xml")
    pisitools.insinto("/usr/share/xvidcap/help/de/figures", "doc/xvidcap/de/figures/*.png")
    pisitools.insinto("/usr/share/xvidcap/help/de/figures", "doc/xvidcap/de/*.xml")
    pisitools.insinto("/usr/share/xvidcap/help/es/figures", "doc/xvidcap/es/figures/*.png")
    pisitools.insinto("/usr/share/xvidcap/help/es/figures", "doc/xvidcap/es/*.xml")
    pisitools.insinto("/usr/share/xvidcap/help/it/figures", "doc/xvidcap/it/figures/*.png")
    pisitools.insinto("/usr/share/xvidcap/help/it/figures", "doc/xvidcap/it/*.xml")
    pisitools.insinto("/usr/share/locale/de/LC_MESSAGES/", "po/de.gmo", "xvidcap.gmo")
    pisitools.insinto("/usr/share/locale/es/LC_MESSAGES/", "po/es.gmo", "xvidcap.gmo")
    pisitools.insinto("/usr/share/locale/en/LC_MESSAGES/", "po/en.gmo", "xvidcap.gmo")
    pisitools.insinto("/usr/share/locale/it/LC_MESSAGES/", "po/it.gmo", "xvidcap.gmo")
    pisitools.insinto("/usr/share/xvidcap/glade/", "src/gnome-xvidcap.glade")
    pisitools.insinto("/usr/share/pixmaps/", "src/pixmaps/xvidcap_logo.png")    
    pisitools.insinto("/usr/share/xvidcap/", "ppm2mpeg.sh")
    pisitools.insinto("/usr/share/xvidcap/omf/", "doc/xvidcap/C/xvidcap-C.omf")
    pisitools.insinto("/usr/share/xvidcap/omf/", "doc/xvidcap/de/xvidcap-de.omf")
    pisitools.insinto("/usr/share/xvidcap/omf/", "doc/xvidcap/es/xvidcap-es.omf")
    pisitools.insinto("/usr/share/xvidcap/omf/", "doc/xvidcap/it/xvidcap-it.omf")
    pisitools.insinto("/usr/share/man/man1/C/", "doc/man/C/*.1")
    pisitools.insinto("/usr/share/man/man1/de/", "doc/man/de/*.1")
    pisitools.insinto("/usr/share/man/man1/es/", "doc/man/es/*.1")
    pisitools.insinto("/usr/share/man/man1/it/", "doc/man/it/*.1")
    
    pisitools.dodoc( "ChangeLog", "COPYING", "AUTHORS", "NEWS", "README")