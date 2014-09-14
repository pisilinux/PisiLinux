#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os


def makedepends(d):
    for root, dirs, files in os.walk(d):
        for name in files:
            if name == "Makefile":
                shelltools.touch(os.path.join(root, "depend.mk"))

def setup():
    pisitools.dosed("config.mk", "^STRIPFLAG.*=.*", "STRIPFLAG = ")

    # force external jasper usage
    pisitools.echo("config.mk", "JASPERLIB = -ljasper")
    pisitools.echo("config.mk", "JASPERHDR_DIR = /usr/include/jasper")

    makedepends("./")

def build():
    autotools.make('CFLAGS="%s -fPIC -O3 -ffast-math -pedantic -fno-common" LDFLAGS="%s" -j1' % (get.CFLAGS(), get.LDFLAGS()))

def install():
    pisitools.dodir("/")
    autotools.make('-j1 package pkgdir=%s/usr' % get.installDIR())

    pisitools.remove("/usr/bin/manweb")

    for data in ["VERSION","pkginfo","README","config_template"]:
        pisitools.remove("/usr/%s" % data)

    pisitools.domove("/usr/man", "/usr/share")

    # remove conflicts with jbigkit
    for i in ["pbm", "pgm"]:
        pisitools.remove("/usr/share/man/man5/%s.5" % i)

    pisitools.dodoc("README", "doc/*LICENSE*")
