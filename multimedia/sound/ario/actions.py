#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt 

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.util import join_path
import piksemel
import os
import fnmatch

def setup():
    shelltools.system("./configure --prefix=/usr --enable-python LDFLAGS=-lm")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "README")

