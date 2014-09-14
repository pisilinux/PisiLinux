#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    for i in ["base", "dicts"]:
        pisitools.insinto("/usr/share/texmf-site/tex/latex/%s" % get.srcNAME(), "%s/*" % i)
        pisitools.dodoc("ChangeLog", "README", "doc/English/*")

