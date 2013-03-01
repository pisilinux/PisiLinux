#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="%s%s" % (get.srcNAME(), get.srcVERSION().replace(".",""))

def build():
    autotools.make('-f unix/Makefile LF2="" CC="%s" CF="%s -I. -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64" unzips' % (get.CC(),get.CFLAGS()))

def install():
    for bin in ["unzip", "funzip", "unzipsfx", "unix/zipgrep"]:
        pisitools.dobin(bin)

    pisitools.dosym("/usr/bin/unzip", "/usr/bin/zipinfo")

    pisitools.doman("man/*.1")
    pisitools.dodoc("BUGS", "History*", "README", "ToDo", "WHERE")
