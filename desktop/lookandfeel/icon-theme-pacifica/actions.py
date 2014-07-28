#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "./"

def install():
  
    shelltools.chmod("%s/pacifica-icon-theme-master/Pacifica/*" % get.workDIR())
    pisitools.insinto("/usr/share/icons", "pacifica-icon-theme-master/Pacifica")
    
#    pisitools.dodoc("AUTHORS", "LICENSE")
