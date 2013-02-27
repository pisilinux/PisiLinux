#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "tdb-%s" % get.srcVERSION()

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--enable-python")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("docs/README")
