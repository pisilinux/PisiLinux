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

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.system("./autogen.sh --prefix=/usr \
				    --sysconfdir=/etc \
				    --localstatedir=/var \
				    --enable-unique \
				    --disable-static \
				    --enable-introspection \
				    --libexecdir=/usr/lib/mate-file-manager")



def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.remove("/usr/share/mime/mime.cache")
    pisitools.remove("/usr/share/mime/globs")
    pisitools.remove("/usr/share/mime/aliases")
    pisitools.remove("/usr/share/mime/types")
    pisitools.remove("/usr/share/mime/magic")
    pisitools.remove("/usr/share/mime/subclasses")
    pisitools.remove("/usr/share/mime/treemagic")
    pisitools.remove("/usr/share/mime/XMLnamespaces")
    pisitools.remove("/usr/share/mime/generic-icons")
    pisitools.remove("/usr/share/mime/globs2")
    pisitools.remove("/usr/share/mime/icons")
    pisitools.remove("/usr/share/mime/version")
