#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

def install():
    pisitools.dobin("gvtray")
    pisitools.dodir("/usr/share/%s/gvtray_about" % get.srcNAME())
    for i in os.listdir("%s/%s/gvtray_about/" % (get.workDIR(), get.srcDIR())):
        pisitools.insinto("usr/share/%s/gvtray_about" % get.srcNAME(), "gvtray_about/%s" % i)
    pisitools.insinto("usr/share/%s" % get.srcNAME(), "gvtray.py")
