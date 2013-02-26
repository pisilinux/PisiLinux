#/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/lib/*.a")
    pisitools.removeDir("/usr/share/doc/wordnet/ps")
    pisitools.domove("/usr/share/wnres", "/usr/share/wordnet")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "LICENSE", "README")
