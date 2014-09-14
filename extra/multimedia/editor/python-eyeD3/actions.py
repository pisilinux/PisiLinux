#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules

WorkDir = "eyeD3-%s" % get.srcVERSION()

def setup():
    #Fix docdir
    pisitools.dosed("Makefile.in", "doc/\${DIST_NAME}", "doc/python-eyeD3")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
