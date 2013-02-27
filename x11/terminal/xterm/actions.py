# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure(" \
             --disable-full-tgetent \
             --with-app-defaults=/usr/share/X11/app-defaults \
             --disable-desktop \
             --with-utempter \
             --with-tty-group=tty \
             --enable-256-color \
             --enable-exec-xterm \
             --enable-freetype \
             --enable-luit \
             --enable-wide-chars \
             --enable-warnings \
            ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/pixmaps")

    pisitools.dodoc("README.i18n", "xterm.log.html", "ctlseqs.txt", "16colors.txt")
