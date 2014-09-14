#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "logilab-astng-%s" % get.srcVERSION()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.removeDir("/usr/lib/%s/site-packages/logilab/astng/test" % get.curPYTHON())

    # Provided by python-logilab-common
    pisitools.remove("/usr/lib/%s/site-packages/logilab/__init__.*" % get.curPYTHON())
