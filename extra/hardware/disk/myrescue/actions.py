#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir="myrescue-0.9.4"

def build():
    shelltools.system("cd src && make")
    

def install():
    pisitools.dobin("src/myrescue")
    pisitools.dodir("/usr/share/man")
    pisitools.insinto("/usr/share/man", "doc/*")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "TODO", "README")
