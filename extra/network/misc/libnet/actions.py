#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

exampledir = "/%s/%s/examples" % (get.docDIR(), get.srcNAME())

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.doman("doc/man/man3/*.3")
    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("README")

    for i in shelltools.ls("doc/*"):
        if shelltools.isFile(i):
            pisitools.dodoc(i)

    pisitools.dodir(exampledir)
    for i in shelltools.ls("sample/*"):
        if i.endswith(".h") or i.endswith(".c"):
            pisitools.insinto(exampledir, i)

