#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def check():
    autotools.make("test")

def install():
    autotools.rawInstall("PREFIX=%s/usr mandir=%s/usr/share/man install install-doc" % ((get.installDIR(),)*2))

    pisitools.dodoc("COPYING", "Documentation/HOWTO")
