#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
    pisitools.insinto("/lib/firmware","*")
    pisitools.insinto("/lib/firmware","bfa_fw_update_to_v3.2.21.1/*")
    
    pisitools.removeDir("/lib/firmware/bfa_fw*")
    pisitools.remove("/lib/firmware/LICENSE")
    
    pisitools.dodoc("LICENSE")
