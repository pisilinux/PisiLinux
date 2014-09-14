#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-xscreensaver \
                         --with-freetype \
                         --with-pango \
                         --with-cspice \
                         --with-gif \
                         --with-jpeg \
                         --with-png \
                         --with-pnm \
                         --with-tiff")


def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "TODO")
