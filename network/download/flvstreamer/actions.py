#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


WorkDir="."


def install():
    shelltools.cd("flvstreamer")
    shelltools.system("make linux")
    pisitools.dobin("flvstreamer")
    pisitools.dobin("streams")
    pisitools.dodoc("README")
