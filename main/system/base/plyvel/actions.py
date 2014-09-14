#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    pythonmodules.install()
    shelltools.chmod("%s/usr/lib/python2.7/site-packages/plyvel-0.8-py2.7.egg-info/top_level.txt" % get.installDIR(), 0644)
    pisitools.dodoc("*.rst")
