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

WorkDir = "mp4v2-%s" % get.srcVERSION()

# autoreconf breaks sandbox with subversion
shelltools.export("HOME", get.workDIR())

def setup():
    #autotools.autoreconf("-vfi")
    autotools.configure("--disable-dependency-tracking \
                         --disable-static \
                         --enable-util \
                         --disable-gch")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "doc/*.txt")
