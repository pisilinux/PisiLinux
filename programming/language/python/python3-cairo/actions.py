#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))

def setup():
    shelltools.export("PYTHON","/usr/bin/python3")
    shelltools.system("python3 ./waf configure --prefix=/usr --libdir=/usr/lib")

def build():
    shelltools.system("python3 waf build -v")

def install():
    shelltools.system("DESTDIR=%s python3 waf install" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "README","COPYING*")