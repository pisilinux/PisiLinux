# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "broadcom-wl-%s" % get.srcVERSION()

def install():
    pisitools.dodir("/lib/firmware")

    for obj in ("../wl_apsta-3.130.20.0.o", "linux/wl_apsta.o"):
        shelltools.system("b43-fwcutter -w %s/lib/firmware %s" % (get.installDIR(), obj))
