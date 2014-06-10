#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("defaults/defaults", "(use_compositing=).*", r"\1true")
    autotools.configure("--prefix=/usr \
                         --disable-static \
                         --enable-startup-notification \
                         --enable-randr \
                         --enable-compositor \
                         --enable-xsync \
                         --disable-debug")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COMPOSITOR", "COPYING", "NEWS", "README", "TODO")
