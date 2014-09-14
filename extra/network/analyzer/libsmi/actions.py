#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

pibsdir = "/usr/share/pibs"

def setup():
    shelltools.export("CFLAGS", "%s -O2" % get.CFLAGS())

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --enable-shared \
                         --enable-smi \
                         --enable-sming")

def build():
    autotools.make()

def check():
    shelltools.export("LC_ALL", "C")
    autotools.make("-j1 check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir(pibsdir)
    for i in ["ietf", "site", "tubs"]:
        pisitools.insinto(pibsdir, "pibs/%s" % i)
        pisitools.remove("%s/%s/Makefile*" % (pibsdir, i))

    pisitools.dodoc("smi.conf-example", "ANNOUNCE", "ChangeLog", "README", "THANKS", "TODO", "doc/*.txt", "doc/smi*")

