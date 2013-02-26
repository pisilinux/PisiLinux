#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

def install():
    for d in ["bora_green", "bora_blue", "bora_black", "zimek_green", "zimek_bisque", \
              "zimek_darkblue", "green_tea", "ostrich", "carp", "arch", "bloe"]:
        pisitools.unlinkDir(d)

    pisitools.insinto("/usr/share/fluxbox/styles/", "*")

    pisitools.dodoc("License")
