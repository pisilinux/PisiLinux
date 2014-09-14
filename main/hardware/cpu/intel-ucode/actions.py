#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    autotools.compile("-Wall %s -o intel-microcode2ucode intel-microcode2ucode.c" % get.CFLAGS())
    shelltools.system("./intel-microcode2ucode ./microcode.dat")

def install():
    pisitools.insinto("/lib/firmware/intel-ucode", "intel-ucode/*")
