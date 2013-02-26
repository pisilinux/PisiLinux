#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --disable-static \
                         --enable-cli \
                         --enable-gtk \
                         --enable-libnotify \
                         --enable-daemon")


def build():
    autotools.make()

    shelltools.cd("qt/")
    shelltools.system("qmake qtr.pro")
    autotools.make()


def install():
    # qt
    autotools.rawInstall("-C qt INSTALL_ROOT=%s/usr" % get.installDIR())
    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()),
                       "qt/README.txt", "README-QT")

    # gtk
    autotools.rawInstall("-C gtk DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C po DESTDIR=%s" % get.installDIR())

    # cli,web, deamon
    for _dir in ["cli", "daemon", "web", "utils"]:
        autotools.rawInstall("-C %s DESTDIR=%s" % (_dir, get.installDIR()))

    # For daemon config files.
    pisitools.dodir("/etc/transmission-daemon")

    pisitools.dodoc("COPYING", "AUTHORS", "README", "NEWS")
