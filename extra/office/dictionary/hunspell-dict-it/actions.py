#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/hunspell", "*.dic")
    pisitools.insinto("/usr/share/hunspell", "*.aff")

    pisitools.dosym("it_IT.dic", "/usr/share/hunspell/it_CH.dic")
    pisitools.dosym("it_IT.aff", "/usr/share/hunspell/it_CH.aff")

    pisitools.dodoc("*.txt", "*AUTHORS", "*ChangeLog", "*COPYING")
