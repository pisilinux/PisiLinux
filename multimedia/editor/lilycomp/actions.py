#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "lilycomp.%s" % get.srcVERSION()

def install():
    pisitools.dobin("lilycomp.py")
    pisitools.rename("/usr/bin/lilycomp.py", "lilycomp")
    pisitools.dohtml("*.html")
    pisitools.dodoc("CHANGES", "COPYRIGHT", "LICENSE")
