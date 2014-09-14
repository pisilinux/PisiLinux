#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("MCS=/usr/bin/dmcs ./autogen.sh --prefix=/usr \
                        --disable-docs \
                        --disable-static \
                        --disable-scrollkeeper \
                        --disable-boo \
                        --disable-youtube \
                        --disable-appledevice \
                        --with-vendor-build-id=PisiLinux")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ") 

def build():
    autotools.make()

def install():
    shelltools.export("MONO_SHARED_DIR", "/usr/lib/mono/")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.move("%s/%s/*" % (get.installDIR(), get.installDIR()), "%s/usr/lib/banshee/" % get.installDIR())
    pisitools.dodoc("AUTHORS","ChangeLog", "COPYING", "NEWS", "README")
    pisitools.removeDir("/var")
