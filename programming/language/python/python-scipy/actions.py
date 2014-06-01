#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

options="config_fc --fcompiler=gnu95"

def install():
    shelltools.export("LDFLAGS","%s -shared" % get.LDFLAGS())


    pythonmodules.install(options)

    pisitools.dodoc("LICENSE.txt","THANKS.txt")
