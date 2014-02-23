#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.system("xmkmf")
    shelltools.system("sed -i 's/#define XAW3D/XCOMM #define XAW3D/' Imakefile")
    shelltools.system("sed -i 's/XCOMM USEINLINE/USEINLINE/' Imakefile")
    shelltools.system("sed -i -e 's/XCOMM #define I18N/#define I18N/' \
           -e 's/XCOMM XAW_INTERN/XAW_INTERN/' Imakefile")
    pisitools.dosed("xfig.desktop", "Name=xfig", "Name=xfig\nIcon=xfig")
    pisitools.dosed("xfig.desktop", "image/x-xfig;", "image/fig;x-xfig;")
    autotools.make('CC="%s" LOCAL_LDFLAGS="%s" CDEBUGFLAGS="%s" XFIGDOCDIR=/usr/share/doc/xfig LIBDIR=/usr/lib XAPPLOADDIR=/usr/share/X11/app-defaults' % (get.CC(), get.LDFLAGS(), get.CFLAGS()))
    
    shelltools.chmod("Libraries", 0755)
    shelltools.system("groff -mandoc -Thtml Doc/xfig.man > Doc/xfig_man.html")

def install():
    autotools.make('DESTDIR=%s XFIGDOCDIR=/usr/share/doc/xfig LIBDIR=/usr/lib XAPPLOADDIR=/usr/share/X11/app-defaults install.all' % get.installDIR())
    
    shelltools.system('find "%s/usr/lib/xfig/Libraries" -type f -exec chmod 0644 {} \;' % get.installDIR())
    shelltools.system('find "%s/usr/lib/xfig/Libraries" -type d -exec chmod 0755 {} \;' % get.installDIR())
    shelltools.system('find "%s/usr/share/doc/xfig" -type f -exec chmod 0644 {} \;' % get.installDIR())
    shelltools.system('find "%s/usr/share/doc/xfig" -type d -exec chmod 0755 {} \;' % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "xfig.png")
    pisitools.insinto("/usr/share/applications", "xfig.desktop")
    pisitools.removeDir("/etc")
