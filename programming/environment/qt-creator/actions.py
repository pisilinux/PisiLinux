#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import qt4

WorkDir = "%s-%s-src" % (get.srcNAME(), get.srcVERSION().replace('_','-'))

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    shelltools.export("HOME", get.curDIR())
    autotools.install("INSTALL_ROOT=%s/usr" % get.installDIR())
    pisitools.dobin("bin/qtcreator")

