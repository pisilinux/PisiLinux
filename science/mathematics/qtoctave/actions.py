#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "qtoctave-0.9.1"

def setup():
    cmaketools.configure("-DCMAKE_SKIP_RPATH:STRING=ON")

def build():
    cmaketools.make("-j1")

def install():
    cmaketools.install()

    pisitools.removeDir("%s/octave-html" % get.docDIR())

    pisitools.dodoc("LICENSE_GPL.txt", "readme.txt")
