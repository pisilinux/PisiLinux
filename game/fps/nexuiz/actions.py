#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# we get sources from the release zipfile

def setup():
    pisitools.dosed("darkplaces/makefile.inc", "pardusCC", get.CC())
    pisitools.dosed("darkplaces/makefile.inc", "pardusCFLAGS", "%s -fno-strict-aliasing -ffast-math -funroll-loops " % get.CFLAGS())
    pisitools.dosed("darkplaces/makefile.inc", "pardusLDFLAGS", "%s -lm" % get.LDFLAGS())

def build():
    shelltools.cd("darkplaces")
    for f in ["cl-nexuiz", "sdl-nexuiz", "sv-nexuiz"]:
        autotools.make("%s DP_FS_BASEDIR=/usr/share/quake1" % f)

def install():
    for f in ["nexuiz-glx", "nexuiz-sdl", "nexuiz-dedicated"]:
        pisitools.dobin("darkplaces/%s" % f)

    pisitools.dosym("nexuiz-sdl", "/usr/bin/nexuiz")

