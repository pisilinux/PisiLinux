#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    pisitools.cxxflags.add("-fno-strict-aliasing")
    autotools.make("clean")
    autotools.make()

def install():
    pisitools.dobin("id3v2")
    pisitools.doman("id3v2.1")

    pisitools.dodoc("COPYING", "README")
