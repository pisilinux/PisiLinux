#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="Gentium Basic 1.1"

def install():
    shelltools.chmod("*.txt",0644)
    shelltools.chmod("*.ttf",0644)

    pisitools.insinto("/usr/share/fonts/gentium-basic/","*.ttf")

    pisitools.dosym("../conf.avail/59-sil-gentium-basic-book.conf", "/etc/fonts/conf.d/59-sil-gentium-basic-book.conf")
    pisitools.dosym("../conf.avail/59-sil-gentium-basic.conf", "/etc/fonts/conf.d/59-sil-gentium-basic.conf")

    pisitools.dodoc("*.txt")
