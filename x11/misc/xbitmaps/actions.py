# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    # Fix conflict with xorg-app
    pisitools.remove("/usr/include/X11/bitmaps/black6")
    pisitools.remove("/usr/include/X11/bitmaps/box6")
