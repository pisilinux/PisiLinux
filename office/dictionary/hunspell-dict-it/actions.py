#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/hunspell", "*.dic")
    pisitools.insinto("/usr/share/hunspell", "*.aff")

    pisitools.dosym("it_IT.dic", "/usr/share/hunspell/it_CH.dic")
    pisitools.dosym("it_IT.aff", "/usr/share/hunspell/it_CH.aff")

    pisitools.dodoc("*.txt", "*AUTHORS", "*ChangeLog", "*COPYING")
