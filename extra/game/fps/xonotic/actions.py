#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Xonotic"

def build():
    autotools.make("-C source/darkplaces CPUOPTIMIZATIONS=\"${CFLAGS}\" DP_FS_BASEDIR=/usr/share/xonotic/ DP_LINK_TO_LIBJPEG=1 cl-release")
    autotools.make("-C source/darkplaces CPUOPTIMIZATIONS=\"${CFLAGS}\" DP_FS_BASEDIR=/usr/share/xonotic/ DP_LINK_TO_LIBJPEG=1 sdl-release")
    autotools.make("-C source/darkplaces CPUOPTIMIZATIONS=\"${CFLAGS}\" DP_FS_BASEDIR=/usr/share/xonotic/ DP_LINK_TO_LIBJPEG=1 sv-release")

def install():
    # autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dobin("source/darkplaces/darkplaces-dedicated")
    pisitools.dobin("source/darkplaces/darkplaces-glx")
    pisitools.dobin("source/darkplaces/darkplaces-sdl")

    pisitools.rename("/usr/bin/darkplaces-dedicated", "xonotic-dedicated")
    pisitools.rename("/usr/bin/darkplaces-glx", "xonotic-glx")
    pisitools.rename("/usr/bin/darkplaces-sdl", "xonotic-sdl")

    pisitools.insinto("/usr/share/pixmaps", "misc/logos/icons_png/xonotic_512.png", "xonotic.png")

    pisitools.dodoc("COPYING", "GPL-2", "GPL-3")
