#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="amd-ucode-2012-09-10"

def install():
    pisitools.insinto("/lib/firmware/amd-ucode", "microcode_amd.bin")
    pisitools.insinto("/lib/firmware/amd-ucode", "microcode_amd_fam15h.bin")
    pisitools.dodoc("LICENSE")
