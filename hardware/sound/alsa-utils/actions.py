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
    autotools.configure("--prefix=/usr \
                         --sbindir=/sbin \
                         --disable-xmlto \
                         --with-udev-rules-dir=/usr/lib/udev/rules.d \
                         --disable-alsaconf")

def build():
    autotools.make()
    shelltools.system("cd alsactl")
    autotools.make()
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    
    pisitools.dodoc("ChangeLog", "README", "TODO", "seq/aconnect/README.aconnect", "seq/aseqnet/README.aseqnet")
