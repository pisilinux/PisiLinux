#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    shelltools.cd("po")
    shelltools.system("./update_mo_files")

def install():
    shelltools.system("./install.sh \
                        prefix=/usr \
                        libdir=/usr/lib \
                        DESTDIR=%s" % get.installDIR())

    # Move icon
    pisitools.domove("/usr/share/pixmaps/devede.svg", "/usr/share/icons/hicolor/scalable/apps")

    # drop redundant stuff
    pisitools.remove("/usr/bin/devede-debug")
    pisitools.remove("/usr/share/doc/devede/html/*~")
