#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--bindir=/bin \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for file in shelltools.ls("%s/bin" % get.installDIR()):
        pisitools.dosym("/bin/%s" % file, "/usr/bin/%s" % file)

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
