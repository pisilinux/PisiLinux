#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("CC_Pardus", get.CC())
    shelltools.export("CFLAGS_Pardus", get.CFLAGS())
    shelltools.export("LDFLAGS_Pardus", get.LDFLAGS())

    autotools.make()

def install():
    pisitools.dobin("antiword")

    pisitools.insinto("/usr/share/antiword","Resources/*")
    pisitools.chmod("%s/usr/share/antiword/*" % get.installDIR(), 0644)

    pisitools.doman("Docs/antiword.1")
    pisitools.dodoc("Docs/COPYING","Docs/ChangeLog","Docs/FAQ","Docs/Emacs","Docs/Mutt","Docs/ReadMe","Docs/QandA")
