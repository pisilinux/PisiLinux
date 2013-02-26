#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde4
from pisi.actionsapi import pisitools

shelltools.export("HOME", get.workDIR())

def setup():
    kde4.configure("-DR_HOME=/usr/lib/R")

def build():
    kde4.make()

def install():
    #for installing rbackend mkdir needed directory(for R-2.5.0)
    pisitools.dodir("/usr/lib/R/library")

    kde4.install()

    # TODO: this one seems better than the one in kdelibs
    pisitools.remove("/usr/share/kde4/apps/katepart/syntax/r.xml")

