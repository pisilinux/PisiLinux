# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
