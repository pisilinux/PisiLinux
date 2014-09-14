#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
			 --disable-dependency-tracking \
                         --enable-python \
                         --enable-php ")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()
    autotools.make("check")

    shelltools.cd("doc")
    autotools.make("doxygen-html")

def install():
    autotools.rawInstall("DESTDIR=%(D)s \
                          PYTHON_PREFIX=%(D)s/usr/lib/%(V)s \
                          PYTHON_EXEC_PREFIX=%(D)s/usr/lib/%(V)s" % {"D": get.installDIR(),
                                                                     "V": get.curPYTHON()})

    pisitools.insinto("/usr/share/doc/geos", "doc/doxygen_docs/html")
    pisitools.dodoc("README", "ChangeLog", "AUTHORS", "NEWS", "COPYING")
