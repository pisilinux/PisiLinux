#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/fonts/Type1", "*.afm")
    pisitools.insinto("/usr/share/fonts/Type1", "*.pfb")

    pisitools.dosym("/usr/share/fonts/urw", "/etc/X11/fontpath.d/urw")

    pisitools.dodoc("ChangeLog", "COPYING", "README", "README.tweaks")
