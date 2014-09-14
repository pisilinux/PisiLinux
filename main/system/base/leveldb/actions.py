#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.chmod("build_detect_platform", 0755)
    autotools.make()

def check():
    autotools.make("check")

def install():
    pisitools.dolib_so("libleveldb.so.1.17")
    pisitools.dosym("libleveldb.so.1.17", "/usr/lib/libleveldb.so.1")
    pisitools.dosym("libleveldb.so.1.17", "/usr/lib/libleveldb.so")

    pisitools.insinto("/usr/include", "include/*")
    pisitools.insinto("/usr/include", "helpers/memenv/memenv.h")

    pisitools.dodoc("README", "LICENSE", "NEWS", "AUTHORS")