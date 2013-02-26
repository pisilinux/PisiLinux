#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def install():
    pythonmodules.install()
    pisitools.insinto(examples, "*.py")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("LICENSE", "README*")
