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
    autotools.configure("--disable-scrollkeeper")

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #gnome-doc-utils file conflicts
    pisitools.remove("/usr/lib/python2.7/site-packages/xml2po/modes/ubuntu.py")
    pisitools.remove("/usr/share/xml/mallard/1.0/mallard.rnc")
    pisitools.remove("/usr/share/xml/mallard/1.0/mallard.rng")
    pisitools.remove("/usr/lib/python2.7/site-packages/xml2po/modes/mallard.py")
    pisitools.remove("/usr/lib/python2.7/site-packages/xml2po/__init__.py")
    pisitools.remove("/usr/lib/python2.7/site-packages/xml2po/modes/docbook.py")
    pisitools.remove("/usr/share/pkgconfig/xml2po.pc")
    pisitools.remove("/usr/bin/xml2po")
    pisitools.remove("/usr/lib/python2.7/site-packages/xml2po/modes/xhtml.py")
    pisitools.remove("/usr/lib/python2.7/site-packages/xml2po/modes/__init__.py")
    pisitools.remove("/usr/lib/python2.7/site-packages/xml2po/modes/gs.py")
    pisitools.remove("/usr/share/man/man1/xml2po.1")
    pisitools.remove("/usr/lib/python2.7/site-packages/xml2po/modes/basic.py")
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README")