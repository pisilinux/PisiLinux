#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "cdparanoia-III-10.2"
flags = "%s -I%s/%s/interface -Wno-pointer-sign -Wno-unused -Werror-implicit-function-declaration" % (get.CFLAGS(), get.workDIR(), WorkDir)

def setup():
    #shelltools.cd("cdparanoia-III-10.2")
    #shelltools.move("configure.guess", "config.guess")
    #shelltools.move("configure.sub", "config.sub")

    autotools.autoreconf("-vfi")
    libtools.gnuconfig_update()
    libtools.libtoolize("--force --install")
    autotools.configure()

def build():
    autotools.make('OPT="%s" -j1' % flags)

    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # No static libs
    #pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("COPYING*", "README")
