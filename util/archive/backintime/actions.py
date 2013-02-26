#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.cd("kde4") 
    autotools.configure()

def build():
    shelltools.cd("kde4")
    autotools.make()

def install(): 
    shelltools.cd("kde4")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
