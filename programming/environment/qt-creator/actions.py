#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import qt4

WorkDir = "%s-opensource-src-%s" % (get.srcNAME(), get.srcVERSION().replace('_','-'))

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    shelltools.export("HOME", get.curDIR())
    autotools.install("INSTALL_ROOT=%s/usr" % get.installDIR())
    pisitools.dobin("bin/qtcreator")

