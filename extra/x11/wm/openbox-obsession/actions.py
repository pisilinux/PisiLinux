#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/local/bin/*" , "/usr/bin")
    pisitools.domove("/usr/local/share/obsession/images/*" , "/usr/share/obsession/images")
    pisitools.domove("/usr/local/share/locale/*" , "/usr/share/local")
    pisitools.removeDir("/usr/local")
    pisitools.dodoc("AUTHORS", "COPYING")