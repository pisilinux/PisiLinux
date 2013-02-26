#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-dependency-tracking \
                         --enable-shared \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # it is said code generation stuff is not necessary, so we remove
    #pisitools.removeDir("/usr/lib/cluttermm-0.9")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README*", "NEWS")
