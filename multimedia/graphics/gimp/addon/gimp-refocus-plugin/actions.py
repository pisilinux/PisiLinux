#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():    
    shelltools.export("LDFLAGS", "%s -lm" % get.LDFLAGS())
    autotools.autoreconf("-fi")
    autotools.rawConfigure("--bindir=/usr/lib/gimp/2.0/plug-ins")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
