#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-dependency-tracking \
                         --with-readline \
                         --enable-cache-size=32")

def build():
    autotools.make()

    shelltools.cd("doc")
    autotools.make("html")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/gnugo/*.html")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "TODO", "THANKS", "README")
