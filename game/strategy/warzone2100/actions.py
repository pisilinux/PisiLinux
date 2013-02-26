#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())
mandir = "/usr/share/man"

def setup():
    autotools.configure('--with-icondir=/usr/share/pixmaps \
                         --disable-rpath \
                         --with-backend=qt \
                         --with-distributor="Pardus Anka" \
                         --disable-debug')

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if shelltools.isDirectory("%s/%s" % (get.installDIR(), mandir)):
        pisitools.removeDir(mandir)

