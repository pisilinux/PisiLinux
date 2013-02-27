#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
