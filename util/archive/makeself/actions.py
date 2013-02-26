#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="makeself-2.1.5"
    

def install():
    pisitools.dobin("makeself.sh")
    pisitools.dodir("/usr/share/man")
    pisitools.dodir("/usr/share/makeself")
    pisitools.doexe("makeself-header.sh", "/usr/share/makeself/")
    pisitools.doman("makeself.1")    

    pisitools.dodoc("COPYING", "TODO", "README")
