#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    kde4.configure("-DPYKDEUIC4_ALTINSTALL=TRUE")

def build():
    kde4.make()

def install():
    kde4.install()

    # pykde4uic symlink
    pisitools.dosym("/usr/lib/%s/site-packages/PyQt4/uic/pykdeuic4.py" % get.curPYTHON(), "/usr/bin/pykde4uic")
    # pykdeuic4 symlink (due to -DPYKDEUIC4_ALTINSTALL=TRUE) to fix sandbox violation
    pisitools.dosym("/usr/lib/%s/site-packages/PyQt4/uic/pykdeuic4.py" % get.curPYTHON(), "/usr/bin/pykdeuic4")
