#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def install():
    shelltools.copytree("/var/pisi/kelimeleme-1.1-1/work/Kelimeleme-1.1/Kelimeleme","%s/usr/share/Kelimeleme" % get.installDIR())
    
