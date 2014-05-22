#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

# WorkDir = "lame-398-2"

def setup():
    shelltools.export("AT_M4DIR", get.curDIR())
    autotools.configure("--prefix=/usr \
                         --enable-nasm \
                         --enable-shared")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s" pkghtmldir="/%s/%s/html"' % (get.installDIR(), get.docDIR(), get.srcNAME()))

    pisitools.dodoc("API", "ChangeLog", "HACKING", "README*", "STYLEGUIDE", "TODO", "USAGE")
    pisitools.dohtml("misc/*", "Dll/*")
    pisitools.dobin("misc/mlame")
