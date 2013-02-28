#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CXXFLAGS","%s  -fno-rtti -fno-exceptions" % get.CXXFLAGS())
    autotools.configure("--enable-multibyte \
                         --with-appresdir=/usr/share/X11/app-defaults \
                         --without-x")

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr")
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # required by man
    pisitools.dosym("eqn", "/usr/bin/geqn")
    pisitools.dosym("tbl", "/usr/bin/gtbl")

    pisitools.dodoc("ChangeLog", "NEWS", "PROBLEMS", "PROJECTS", "README")
