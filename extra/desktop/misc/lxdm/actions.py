#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr     \
                         --sysconfdir=/etc \
                         --with-pam        \
                         --with-systemdsystemunitdir=no \
                         --enable-gtk3")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #install Pisi Linux default theme
    pisitools.insinto("/usr/share/lxdm/themes", "lxdm-pisilinux-theme")
    pisitools.remove("/usr/share/lxdm/themes/lxdm-pisilinux-theme/login.png")
    pisitools.dodoc("COPYING", "AUTHORS", "TODO", "README", "ChangeLog", "NEWS")
