#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():

    shelltools.system("./autogen.sh --prefix=/usr \
				    --sysconfdir=/etc \
				    --localstatedir=/var \
				    --disable-update-mimedb \
				    --disable-appindicator")



def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())   

    pisitools.dodoc("README", "COPYING", "NEWS", "ChangeLog", "AUTHORS", "TODO")
    
    pisitools.remove("/usr/share/applications/mimeinfo.cache")
