#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.insinto("/usr/share/megaglest/data", "data/*")
    pisitools.insinto("/usr/share/megaglest/maps", "maps/*")
    pisitools.insinto("/usr/share/megaglest/scenarios", "scenarios/*")
    pisitools.insinto("/usr/share/megaglest/techs", "techs/*")
    pisitools.insinto("/usr/share/megaglest/tilesets", "tilesets/*")
    pisitools.insinto("/usr/share/megaglest/tutorials", "tutorials/*")

    pisitools.dodoc("docs/AUTHORS.data.txt", "docs/cc-by-sa-3.0-unported.txt", "docs/COPYRIGHT.data.txt", "docs/README.data-license.txt")
