#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def install():
    shelltools.copytree("/var/pisi/kelimeleme-1.1-1/work/Kelimeleme-1.1/Kelimeleme","%s/usr/share/Kelimeleme" % get.installDIR())
    
