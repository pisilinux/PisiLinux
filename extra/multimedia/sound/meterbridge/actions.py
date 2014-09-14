#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    pisitools.dosed("src/main.h", "extern SDL_Rect win, buf_rect\[MAX_METERS\]", "extern SDL_Rect win")
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog")
