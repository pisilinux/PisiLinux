#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release", installPrefix="/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    #for f in ["Point.h", "capi/sidx_config.h", "capi/sidx_impl.h"]:
     #         pisitools.dosed("%s/usr/include/libspatialindex/%s" % (get.installDIR(), f), "(#include\s<)spatialindex/", r"\1")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

# By PiSiDo 2.0.0
