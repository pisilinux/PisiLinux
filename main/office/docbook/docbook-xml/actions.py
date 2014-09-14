#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="."

def install():
    for version in ["4.1.2", "4.2", "4.3", "4.4", "4.5"]:
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "*.dtd")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "*.mod")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s" % version, "docbook.cat")
        pisitools.insinto("/usr/share/xml/docbook/xml-dtd-%s/ent" % version, "ent/*.ent")

    pisitools.dodoc("ChangeLog", "README")
