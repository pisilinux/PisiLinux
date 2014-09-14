#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="ttf-bitstream-vera-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/fonts/bitstream-vera/", "*.ttf")
    shelltools.chmod("%s/usr/share/fonts/bitstream-vera/*" % get.installDIR(), 0644)

    pisitools.dodoc("*.TXT")
