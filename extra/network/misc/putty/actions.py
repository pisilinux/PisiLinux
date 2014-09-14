#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.cd("unix") 
    autotools.configure("--prefix=/usr")

def build():
    shelltools.cd("unix")
    autotools.make()

def install():
    shelltools.cd("unix")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd()
    pisitools.dodoc("LICENCE", "README", "doc/puttydoc.txt")
    pisitools.dohtml("doc/*.html")
