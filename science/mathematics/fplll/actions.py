#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="libfplll-%s" % get.srcVERSION()

def setup():
    autotools.configure("--disable-static \
                         --includedir=/usr/include/fplll")

def build():
    autotools.make("clean")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS","COPYING","README","NEWS")
