#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    for i in ["base", "dicts"]:
        pisitools.insinto("/usr/share/texmf-site/tex/latex/%s" % get.srcNAME(), "%s/*" % i)
        pisitools.dodoc("ChangeLog", "README", "doc/English/*")

