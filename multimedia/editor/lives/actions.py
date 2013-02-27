# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #fix doc dir
    pisitools.dosed('Makefile.in',  '^(docdir.*PACKAGE\)).*', r'\1"')
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("COPYING")
    pisitools.remove("/usr/bin/lives")
    pisitools.dosym("/usr/bin/lives-exe", "/usr/bin/lives")
