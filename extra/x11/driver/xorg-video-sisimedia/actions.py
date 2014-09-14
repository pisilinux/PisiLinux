# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/Makefile.am", "sis_drv", "sisimedia_drv")
    pisitools.dosed("src/sis.h", '"sis"', '"sisimedia"')
    pisitools.dosed("src/sis_driver.c", "sisModuleData", "sisimediaModuleData")

    autotools.autoreconf("-vif")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    # Same as sis man page
    pisitools.removeDir("/usr/share/man")
