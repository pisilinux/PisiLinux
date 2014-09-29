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
    autotools.configure("--with-config-file=/etc/GNUstep/GNUstep.conf \
                        --with-layout=fhs \
                        --enable-native-exceptions")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.makedirs("%s/etc/profile.d" % get.installDIR())
    shelltools.copy("GNUstep.sh", "%s/etc/profile.d/GNUstep.sh" % get.installDIR())

    pisitools.dodoc("FAQ", "README", "RELEASENOTES")
