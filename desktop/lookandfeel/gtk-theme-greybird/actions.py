#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

	
def install():
    pisitools.dodir ("/usr/share/themes/Greybird")

    for subtheme in ["gtk-2.0", "gtk-3.0", "metacity-1", "xfwm4"]:
        pisitools.insinto ("/usr/share/themes/Greybird", subtheme)

    pisitools.dodoc ("LICENSE.CC", "LICENSE.GPL")
