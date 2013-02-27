#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    autotools.install("DESTDIR=%s PREFIX=/usr" % get.installDIR())

    pisitools.remove("/usr/lib/libacpi.a")
    pisitools.removeDir("/usr/share/doc/libacpi")

    pisitools.dohtml("doc/html/*")

    pisitools.dodoc("AUTHORS", "CHANGES", "LICENSE", "README", "TODO")
