#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static\
                         --disable-skdb-update\
                         --enable-scrollkeeper-compat\
                         --enable-omf-read")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/var")
    pisitools.remove("/usr/bin/rarian-example")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README", "MAINTAINERS")
