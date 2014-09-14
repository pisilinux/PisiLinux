#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--libdir=/usr/lib \
                         --sysconfdir=/etc/gpm")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove this when we can break abi
    pisitools.dosym("libgpm.so.2", "/usr/lib/libgpm.so")

    #remove static link
    pisitools.remove("/usr/lib/libgpm.a")

    pisitools.insinto("/etc/gpm", "conf/gpm-*.conf")

    pisitools.dodoc("COPYING", "README", "TODO", "doc/Announce", "doc/FAQ", "doc/README*")
