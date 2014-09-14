#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


data = "/usr/share"
WorkDir = "%s_%s" % (get.srcNAME(), get.srcVERSION())

def setup():
    for f in ["conf.h", "configure", "configure.in", "Makefile", "Makefile.in", "output.1"]:
        pisitools.dosed(f, "games/")

    autotools.autoreconf("-fi")
    autotools.configure("--datadir=%s" % data)

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/bin")
    autotools.install('exec_prefix="%s/usr" datadir="%s/%s"' % (get.installDIR(), get.installDIR(), data))

    pisitools.dodoc("README.txt", "CHANGES.txt")
