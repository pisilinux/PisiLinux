#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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
