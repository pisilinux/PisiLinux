#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def setup():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodir("/etc/bash_completion.d")
    pisitools.insinto("/etc/bash_completion.d", "contrib/bash_completion", "mercurial")

    pisitools.doman("doc/*.1")
    pisitools.doman("doc/*.5")

    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("doc/*.txt")
