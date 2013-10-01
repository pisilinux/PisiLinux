#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--prefix=/usr --x-includes=/usr/include --x-libraries=/usr/lib")
                        

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("datainstall DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps/", "Ticon.png", "torcs.png")    # Desktop/pisi icon file
    # pisitools.remove("/usr/share/torcs/COPYING")    # Will be included in documentation

    pisitools.dodoc("doc/history/history.txt","COPYING","README")
    pisitools.doman("doc/man/*.6")
