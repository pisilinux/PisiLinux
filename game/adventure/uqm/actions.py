#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "%s-%s/sc2" % (get.srcNAME(), get.srcVERSION())

def setup():
    pisitools.dosed("build.vars", "pardusCFLAGS", get.CFLAGS())
    pisitools.dosed("build.vars", "pardusLDFLAGS", get.LDFLAGS())

def build():
    shelltools.system("sh build.sh uqm")

def install():
    pisitools.dobin("uqm", "/usr/share/uqm")
    pisitools.insinto("/usr/share/uqm/content", "content/version")
    pisitools.dodoc("README", "COPYING", "AUTHORS", "doc/users/manual.txt")

