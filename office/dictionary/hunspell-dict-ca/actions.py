#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "hunspell"

def setup():
    pisitools.dosed("catalan.aff", "\r")
    pisitools.dosed("catalan.dic", "\r")

def install():
    for lang in ("ca_AD", "ca_FR", "ca_IT", "ca_ES"):
        pisitools.insinto("/usr/share/hunspell", "catalan.aff", lang + ".aff")
        pisitools.insinto("/usr/share/hunspell", "catalan.dic", lang + ".dic")

    pisitools.dohtml("release-notes*")
