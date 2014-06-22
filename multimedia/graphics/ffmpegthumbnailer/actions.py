#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("libffmpegthumbnailer/pngwriter.cpp", "#include <cassert>", "#include <cassert>\n#include <cstring>")
    autotools.configure("--disable-static \
                         --enable-png \
                         --enable-jpeg")

def build():
    autotools.make()

def install():
    autotools.install()

    # Empty files: NEWS, TODO
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
