#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --without-ibmtts \
                         --without-nas \
                         --with-flite \
                         --with-alsa \
                         --with-espeak \
                         --with-libao \
                         --with-pulse")

def build():
    autotools.make()

def install():
    autotools.install()

    # Remove redundant conf files
    pisitools.removeDir("/usr/share/opentts")

    pisitools.dodoc("AUTHORS", "COPYING", "README")

