#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="Imaging-%s" % get.srcVERSION()

def install():
    pisitools.dosed("_imagingft.c", "<freetype/freetype.h>", "<freetype2/freetype.h>")
    pisitools.dosed("_imagingft.c", "<freetype/fterrors.h>", "<freetype2/fterrors.h>")
    pythonmodules.install()

    shelltools.cd("Sane")
    pythonmodules.install()
    shelltools.cd("..")

    for header in ["Imaging.h","ImPlatform.h"]:
        pisitools.insinto("/usr/include/%s" % get.curPYTHON(), "libImaging/%s" % header)

    pisitools.dodoc("README")

