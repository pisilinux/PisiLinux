#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "libxml++-%s" % get.srcVERSION()

def setup():
    autotools.configure("--disable-static \
                         --disable-examples \
                         --enable-dependency-tracking")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ") 
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("docs/reference/html/*")

    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README*")
    #pisitools.removeDir("/usr/share/doc/libxml++-2.6")
