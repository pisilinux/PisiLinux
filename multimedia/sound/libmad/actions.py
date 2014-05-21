#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.cflags.add("-ftree-vectorize -ftree-vectorizer-verbose=1")
    for i in ["NEWS", "AUTHORS", "ChangeLog"]:
        shelltools.touch(i)

    autotools.autoreconf("-vfi")

    autotools.configure("--disable-debugging \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("CHANGES", "COPYRIGHT", "CREDITS", "README", "TODO", "VERSION")
