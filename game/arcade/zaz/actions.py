#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2010-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-rpath")

    # Remove zaz.pot so that make will create pot and catalog files
    shelltools.unlink("po/zaz.pot")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/share/doc/zaz/INSTALL")
