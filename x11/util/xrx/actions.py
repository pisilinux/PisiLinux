#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")

    shelltools.export("PLUGIN_CFLAGS" , "%s/plugin/include" % get.srcDIR())

    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.domove("/usr/lib/*.so" ,"/usr/lib/browser-plugins")

    pisitools.dodoc("COPYING", "ChangeLog", "README")
