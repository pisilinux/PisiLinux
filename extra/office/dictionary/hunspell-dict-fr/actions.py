#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/hunspell", "*.dic")
    pisitools.insinto("/usr/share/hunspell", "*.aff")

    shelltools.chmod("%s/usr/share/hunspell/*" % get.installDIR(), 0644)

    for lang in ("fr_BE", "fr_CA", "fr_CH", "fr_LU", "fr_MC"):
        pisitools.dosym("fr_FR.dic", "/usr/share/hunspell/%s.dic" % lang)
        pisitools.dosym("fr_FR.aff", "/usr/share/hunspell/%s.aff" % lang)

    pisitools.dodoc("README*")
