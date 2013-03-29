#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    autotools.configure()
    
def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.domo("po/it.po", "it", "font-manager.mo")
    pisitools.domo("po/ru.po", "ru", "font-manager.mo")
    pisitools.domo("po/sk.po", "sk", "font-manager.mo")
    pisitools.dodoc("README","COPYING","INSTALL")
