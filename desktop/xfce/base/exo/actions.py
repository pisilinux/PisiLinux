#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
#    shelltools.system('NOCONFIGURE=1 xdt-autogen')
    autotools.configure("--sysconfdir=/etc \
                         --libexecdir=/usr/lib/xfce4 \
                         --localstatedir=/var \
                         --disable-static \
                         --disable-debug")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
