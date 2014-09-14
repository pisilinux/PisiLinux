#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("gui/mdmsetup.desktop.in.in", "gksu", "xdg-su -c")
    shelltools.system(" ./autogen.sh  --with-prefetch \
                    --prefix=/usr \
                    --with-console-kit=yes \
                    --enable-authentication-scheme=pam \
                    --sysconfdir=/etc \
                    --localstatedir=/var \
                    --disable-static \
                    --with-xinerama=yes \
                    --with-libaudit=yes \
                    --with-xevie=yes \
                    --with-log-dir=/var/lib/mdm \
                    --disable-scrollkeeper \
                    --enable-compile-warnings=no \
                    --sbindir=/usr/sbin")

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #install Pisi Linux theme
    pisitools.insinto("/usr/share/mdm/themes", "PisiLinux")

    #remove empty folders
    pisitools.removeDir("/usr/share/xsessions/")
    pisitools.removeDir("/etc/dm/")

    #move conflict files
    pisitools.domove("/usr/share/pixmaps","/usr/share/mdm")

    #move .desktop files
    pisitools.domove("/usr/share/mdm/applications/*.desktop","/usr/share/applications")
    pisitools.remove("/usr/share/applications/mdmflexiserver.desktop")
    pisitools.removeDir("/usr/share/mdm/applications/")



    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")



