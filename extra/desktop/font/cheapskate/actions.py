#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import glob

def install():
    for z in glob.glob ("*.zip"):
        shelltools.system("unzip -o %s"% z)
    pisitools.insinto("/usr/share/fonts/cheapskate", "*.ttf")

    pisitools.dodoc("license.txt")
