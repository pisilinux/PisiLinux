#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="."

def install():
    pisitools.insinto("/usr/share/sgml/docbook/sgml-dtd-%s" % get.srcVERSION(), "*.dcl")
    pisitools.insinto("/usr/share/sgml/docbook/sgml-dtd-%s" % get.srcVERSION(), "*.dtd")
    pisitools.insinto("/usr/share/sgml/docbook/sgml-dtd-%s" % get.srcVERSION(), "*.mod")
    pisitools.insinto("/usr/share/sgml/docbook/sgml-dtd-%s" % get.srcVERSION(), "docbook.cat", "catalog")

    pisitools.dodoc("ChangeLog")
