#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "simplejson-%s" % get.srcVERSION()

def install():
    pythonmodules.install()

    #pisitools.insinto("%s/%s/html" % (get.docDIR(), get.srcNAME()))
    pisitools.dodoc("LICENSE.txt")
