#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "libevent-%s-stable" % get.srcVERSION()

def setup():
    pisitools.dosed("Makefile.am", "libevent_extra_la_LIBADD =", "libevent_extra_la_LIBADD = libevent.la ")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README")
