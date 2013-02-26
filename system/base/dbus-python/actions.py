#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build-python2")
    shelltools.makedirs("build-python3")
    autotools.autoreconf("-fi")

    shelltools.cd("build-python3")
    shelltools.system("PYTHON=python3 ../configure --prefix=/usr \
                       --localstatedir=/var \
                       --disable-api-docs \
                       --disable-html-docs \
                       --disable-static")

    shelltools.cd("../build-python2")
    shelltools.system("../configure --prefix=/usr \
                       --localstatedir=/var \
                       --disable-api-docs \
                       --disable-html-docs \
                       --disable-static")

def build():
    shelltools.cd("build-python3")
    autotools.make()

    shelltools.cd("../build-python2")
    autotools.make()

def check():
    #autotools.make("check")
    pass

def install():
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")

    shelltools.cd("build-python3")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../build-python2")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
