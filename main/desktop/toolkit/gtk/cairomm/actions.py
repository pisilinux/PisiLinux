#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static")
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/devhelp")

    #move html docs to html doc dir
    pisitools.dodir("/usr/share/doc/%s/html" % get.srcNAME())
    pisitools.domove("/usr/share/doc/%s-1.0/*" % get.srcNAME(), "/usr/share/doc/%s/html" % get.srcNAME())
    pisitools.removeDir("/usr/share/doc/%s-1.0" % get.srcNAME())

    pisitools.dodoc("AUTHORS", "README", "COPYING", "ChangeLog", "NEWS")
