#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # autotools.configure("--bindir=%s/bin" % get.installDIR())
    autotools.configure("--prefix=/")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    pisitools.dosym("tcsh", "/bin/csh")

    pisitools.dodoc("FAQ", "Fixes", "NewThings", "Ported", "README", "WishList", "Y2K")
