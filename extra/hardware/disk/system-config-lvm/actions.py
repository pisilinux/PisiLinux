#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure()

def build():
    autotools.make()
    pisitools.dosed("src/system-config-lvm.py", "python2", "python")

def install():
    autotools.install()
    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/etc/security")

