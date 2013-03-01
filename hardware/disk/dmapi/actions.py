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

def setup():
    shelltools.export("OPTIMIZER", get.CFLAGS())
    shelltools.export("DEBUG", "-DNDEBUG")

    autotools.autoconf()
    autotools.configure("--libexecdir=/usr/lib \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DIST_ROOT="%s" install-dev' % get.installDIR())
