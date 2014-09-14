#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())
shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

def build():
    scons.make('PREFIX=/usr \
                COMPILE_FLAGS="%s %s -lpthread" \
                BUILD_TESTS=0' % (get.CXXFLAGS(), get.LDFLAGS()))

def install():
    scons.install("install WILL_DEAL_WITH_XDG_MYSELF=1 DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/applications")
    pisitools.dosym("/usr/share/libffado/icons/hi64-apps-ffado.png", "/usr/share/pixmaps/ffado-mixer.png")

    pisitools.domove("/usr/man/", "/usr/share")

    pisitools.dodoc("AUTHORS", "ChangeLog", "LICENSE*", "TODO", "README")
