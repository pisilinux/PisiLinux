#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

#WorkDir = ""

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./autogen.sh --noconfig")
    autotools.configure("--enable-mysql --enable-fc --enable-efficiency \
                        --enable-snmp --disable-static \
                        --localstatedir=/var")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # remove empty dir
    pisitools.removeDir("/usr/lib/plugins")
