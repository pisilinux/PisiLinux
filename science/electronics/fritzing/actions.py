#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import qt4
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    qt4.configure(installPrefix='%s/usr' % get.installDIR())

def build():
    qt4.make()
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
