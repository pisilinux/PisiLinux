#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # fix test return state
    #pisitools.dosed("regress/open_nonarchive.test", "19/2", "19/0")
    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS","NEWS","README")
    
    # preserve old header path for compatibility
    pisitools.dosym("/usr/lib/libzip/include/zipconf.h", "/usr/include/zipconf.h")
