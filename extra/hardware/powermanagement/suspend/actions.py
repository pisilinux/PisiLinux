# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get



def setup():
    #autotools.autoreconf("-vif")
    autotools.configure("--enable-threads \
                         --enable-compress \
                         --enable-plymouth \
                         --disable-encrypt \
                         --disable-resume-static \
                         --with-initramfsdir=/usr/sbin")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/dev")

    shelltools.touch("%s/etc/suspend.key" % get.installDIR())
