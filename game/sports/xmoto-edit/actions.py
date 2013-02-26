#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir= "extensions"

def install():
    pisitools.insinto("/usr/share/inkscape/extensions", "*")

    pisitools.dodoc("README", "COPYING", "AUTHORS")


