#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyright 2006-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "pcsxr-%s" % get.srcVERSION()
shelltools.export("CFLAGS", "%s -fno-strict-aliasing -pthread -w" % get.CFLAGS())

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-libcdio --enable-opengl")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
