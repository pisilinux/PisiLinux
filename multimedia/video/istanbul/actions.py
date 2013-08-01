#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

import os
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())
shelltools.export("PYTHONDONTWRITEBYTECODE", "1")
def setup():
    os.environ["GST_REGISTRY"] = get.workDIR() + "/registry.cache.xml"
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-gconftool \
                         --disable-schemas-install")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" %get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
