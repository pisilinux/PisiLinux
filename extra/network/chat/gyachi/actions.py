#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

wine_parameter = "--disable-wine" if get.ARCH() == "x86_64" else ""

def setup():
    # _FILE_OFFSET_BITS=64 is needed to compile the package for i686
    shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=64" % get.CFLAGS())

    shelltools.system("sh autogen.sh")
    # disable wine for now, for the 64 bit issues.
    autotools.configure("--disable-rpath \
                         --enable-plugin_pulseaudio \
                         --enable-plugin_blowfish \
                         --enable-plugin_mcrypt \
                         --enable-plugin_gpgme \
                         --enable-plugin_libnotify \
                         --enable-plugin_photo_album \
                         --enable-gtkspell \
                         --disable-plugin_xmms \
                         --disable-esd %s" % wine_parameter)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "themes/gyachi-classic/gyach-icon_48.png", "gyachi.png")
    pisitools.insinto("/usr/share/icons/hicolor/32x32/apps/gyachi", "themes/gyachi-classic/gyach-icon_32.png", "gyachi.png")
    pisitools.insinto("/usr/share/icons/hicolor/48x48/apps/gyachi", "themes/gyachi-classic/gyach-icon_48.png", "gyachi.png")

    pisitools.dodoc("ChangeLog", "VERSION", "doc/*.txt", "doc/txt/COPYING", "doc/txt/README", "doc/txt/webcams.txt", "doc/txt/gyachi-help-short.txt")
    pisitools.dohtml("doc/html/*")
