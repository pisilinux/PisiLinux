#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import scons

def build():
    scons.make("PREFIX=/usr/ LIBDIR=/usr/lib")

def install():
    pisitools.insinto("/usr/include/serf-1/", "serf*.h")
    pisitools.insinto("/usr/lib/", "libserf-1*")
    pisitools.insinto("/usr/lib/pkgconfig/", "serf-1.pc")
    
    pisitools.dodoc("CHANGES", "LICENSE", "NOTICE", "README")