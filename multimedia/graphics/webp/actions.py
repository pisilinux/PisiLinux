#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt
import shutil
import os
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

#shelltools.export("USER","q")
WorkDir="libwebp-0.2.1"

def setup():
    shelltools.system('./configure --prefix=/usr --sysconfdir=/etc --sharedstatedir=/var/lib --localstatedir=/var --disable-static')
  
def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/share/doc/webp")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.move("%s/libwebp-0.2.1/doc/*" % get.workDIR(),"%s/usr/share/doc/webp" % get.installDIR())
    #shelltools.move("%s/libwebp-0.2.1/README" % get.workDIR(),"%s/usr/share/doc/webp" % get.installDIR())
