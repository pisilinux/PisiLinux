#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt 

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

def setup():
    
    autotools.configure("--prefix=/usr \
                         --enable-exp-attack \
                         --enable-semaphore \
                         --enable-sem-open \
                         --enable-memory-barrier")

def build():
    autotools.make()

def install():
   
    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "README")

