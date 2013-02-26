#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())
plugins = "%s/%s/plugins" % (get.dataDIR(), get.srcNAME())

def install():
    pisitools.insinto("/usr/include", "CImg.h")

    pisitools.insinto(examples, "examples/*")
    pisitools.insinto(plugins, "plugins/*")
    pisitools.dohtml("html/*")
    pisitools.dodoc("*.txt")
