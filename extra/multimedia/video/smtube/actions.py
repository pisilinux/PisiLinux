#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def build():
    autotools.make("PREFIX=/usr")

def install():
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("Readme.txt","Release_notes.txt","Changelog","Copying.txt") 
