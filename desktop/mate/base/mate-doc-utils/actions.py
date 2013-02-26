#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.copy("tools/mate-doc-utils.m4", "m4/")
    shelltools.system("./autogen.sh \
                       --prefix=/usr \
                       --disable-scrollkeeper \
                       --sysconfdir=/etc \
                       --mandir=/usr/share/man \
                       --localstatedir=/var")
    autotools.configure()

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README")
    pisitools.remove("/usr/share/mate-doc-utils/mate-debian.sh")

    # remove conflicted files with gnome-doc-utils
    pisitools.removeDir("usr/lib/python2.7/site-packages/xml2po")
    pisitools.remove("usr/bin/xml2po")
    pisitools.remove("usr/share/man/man1/xml2po.1")
    pisitools.remove("usr/share/pkgconfig/xml2po.pc")
    pisitools.removeDir("usr/share/xml/mallard")
