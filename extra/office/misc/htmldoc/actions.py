#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("htmldoc/http-addrlist.c","RESOLV_H \*/","RESOLV_H \*/\n#include <errno.h>")
    autotools.rawConfigure("--prefix={0}/usr".format(get.installDIR()))
    
def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("README.txt","CHANGES.txt")
    pisitools.insinto("/usr/share/applications/","desktop/htmldoc.desktop")
    for i in [16,24,32,48,64,96,128]:
		pisitools.insinto("/usr/share/icons/hicolor/{0}x{0}/apps".format(i),"desktop/htmldoc-{0}.png".format(i),"htmldoc.png")
    pisitools.insinto("/usr/share/mime/packages/","desktop/htmldoc.xml")
