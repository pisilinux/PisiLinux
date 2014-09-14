#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

WorkDir = "v4l2capture-%s" % get.srcVERSION()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.insinto("%s/%s/examples" % (get.docDIR(), get.srcNAME()), "capture_*.py")
    pisitools.insinto("%s/%s/examples" % (get.docDIR(), get.srcNAME()), "list_devices.py")

    pisitools.dodoc("README")
