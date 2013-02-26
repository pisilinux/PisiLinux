#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "xlrd-%s" % get.srcVERSION()

def setup():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    shelltools.chmod("%s/usr/bin/runxlrd.py" % get.installDIR(), 0755)

    pisitools.domove("/usr/lib/%s/site-packages/xlrd/doc/*.html" % get.curPYTHON(), "%s/python-xlrd" % get.docDIR())
    pisitools.removeDir("/usr/lib/%s/site-packages/xlrd/doc/" % get.curPYTHON())
    pisitools.domove("/usr/lib/%s/site-packages/xlrd/examples" % get.curPYTHON(), "%s/python-xlrd" % get.docDIR())
