# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    shelltools.system('sed -e "s/DRI_CFLAGS/DRI1_CFLAGS/g" -i configure')
    autotools.configure("--enable-sna \
                         --with-default-accel=sna \
                         --disable-static \
                         --enable-dri \
                         --enable-glamor")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README")
