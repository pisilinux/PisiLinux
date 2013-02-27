#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("LDFLAGS", "%s -lpthread" % get.LDFLAGS())

    for files in ("AUTHORS", "NEWS", "README"):
        shelltools.touch(files)

    autotools.autoreconf("-fi")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "README.TXT", "LICENSE.MIT", "TODO")
