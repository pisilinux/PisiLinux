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
    for f in ("AUTHORS", "ChangeLog"): shelltools.touch(f)
    autotools.autoreconf("-fiv")
    autotools.configure("--with-mad \
                         --disable-xmms \
                         --with-audiofile")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("NEWS", "README", "THANKS", "TODO")
