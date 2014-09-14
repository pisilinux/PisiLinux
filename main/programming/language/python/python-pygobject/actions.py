#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "pygobject-%s" % get.srcVERSION()

def setup():
    # autoreconf is for under linking problem
    autotools.autoreconf("-fi")
    autotools.configure("--disable-introspection")

def build():
    autotools.make()

def install():
    autotools.install()

    #shelltools.chmod("%s/usr/share/pygobject/xsl/fixxref.py" % get.installDIR(), 0755)
    pisitools.dodoc("AUTHORS", "NEWS", "ChangeLog", "README")
