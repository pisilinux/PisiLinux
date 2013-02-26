#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/hunspell", "ru_myspell.dict", "ru_RU.dic")
    pisitools.insinto("/usr/share/hunspell", "ru_RU.koi8r.aff", "ru_RU.aff")

    shelltools.chmod("%s/usr/share/hunspell/*" % get.installDIR(), 0644)

    for lang in ("ru_UA",):
        pisitools.dosym("ru_RU.dic", "/usr/share/hunspell/%s.dic" % lang)
        pisitools.dosym("ru_RU.aff", "/usr/share/hunspell/%s.aff" % lang)

    pisitools.dodoc("readme*", "LICENSE")
