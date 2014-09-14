#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def install():
    pisitools.dodoc("*.txt", "*TXT")

    pisitools.insinto("/usr/lib/%s/site-packages/%s" % (get.curPYTHON(), get.srcNAME()), "*")
    pisitools.remove("/usr/lib/%s/site-packages/%s/*.txt" % (get.curPYTHON(), get.srcNAME()))
    pisitools.remove("/usr/lib/%s/site-packages/%s/*.TXT" % (get.curPYTHON(), get.srcNAME()))
