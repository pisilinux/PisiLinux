#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/fonts/Type1", "*.afm")
    pisitools.insinto("/usr/share/fonts/Type1", "*.pfb")

    pisitools.dosym("/usr/share/fonts/urw", "/etc/X11/fontpath.d/urw")

    pisitools.dodoc("ChangeLog", "COPYING", "README", "README.tweaks")
