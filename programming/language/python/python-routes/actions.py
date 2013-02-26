#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "Routes-%s" % get.srcVERSION()

def build():
    shelltools.cd("docs")
    autotools.make("html")

def install():
    pythonmodules.install()

    pisitools.dodoc("docs/*.rst")
    pisitools.dohtml("docs/_build/html/*")
