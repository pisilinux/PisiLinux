#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--with-python \
                         --with-gtk=2.0 \
                         --disable-introspection \
                         --disable-plugin \
                         --disable-static")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #remove the empty bin directory
    pisitools.removeDir("/usr/bin")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
