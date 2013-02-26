#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "igerman98-20090107"

def build():
    autotools.make("hunspell/de_AT.dic hunspell/de_AT.aff hunspell/de_CH.dic hunspell/de_CH.aff hunspell/de_DE.dic hunspell/de_DE.aff ")

    shelltools.cd("hunspell")
    for f in ("README_de_AT.txt", "README_de_CH.txt", "README_de_DE.txt"):
        pisitools.dosed(f, "\r")

def install():
    shelltools.cd("hunspell")
    pisitools.insinto("/usr/share/hunspell", "de_??.dic")
    pisitools.insinto("/usr/share/hunspell", "de_??.aff")

    pisitools.dosym("de_DE.dic", "/usr/share/hunspell/de_BE.dic")
    pisitools.dosym("de_DE.aff", "/usr/share/hunspell/de_BE.aff")
    pisitools.dosym("de_DE.dic", "/usr/share/hunspell/de_LU.dic")
    pisitools.dosym("de_DE.aff", "/usr/share/hunspell/de_LU.aff")

    pisitools.dosym("de_CH.dic", "/usr/share/hunspell/de_LI.dic")
    pisitools.dosym("de_CH.aff", "/usr/share/hunspell/de_LI.aff")

    pisitools.dodoc("README*", "COPYING*")
