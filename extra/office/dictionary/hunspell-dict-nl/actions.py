#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def setup():
    shelltools.system("unzip -o nl_NL.zip")

def install():
    pisitools.insinto("/usr/share/hunspell", "*.dic")
    pisitools.insinto("/usr/share/hunspell", "*.aff")

    pisitools.dosym("nl_NL.dic", "/usr/share/hunspell/nl_BE.dic")
    pisitools.dosym("nl_NL.aff", "/usr/share/hunspell/nl_BE.aff")

    pisitools.dodoc("*.txt")
