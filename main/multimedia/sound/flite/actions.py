#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "flite-%s-current" % get.srcVERSION()
   
def setup(): 
    autotools.configure("--prefix=/usr \
                         --with-audio=alsa \
	                 --with-vox=cmu_us_kal16")

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "README")
