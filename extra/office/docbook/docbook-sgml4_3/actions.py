#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="."

def install():
    target = "/usr/share/sgml/docbook/sgml-dtd-%s" % get.srcVERSION()

    pisitools.insinto(target, "*.dcl")
    pisitools.insinto(target, "*.dtd")
    pisitools.insinto(target, "*.mod")
    pisitools.insinto(target, "docbook.cat", "catalog")

    pisitools.dodoc("ChangeLog", "README")
