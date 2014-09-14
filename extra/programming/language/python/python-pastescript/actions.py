#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pythonmodules.install()
    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "docs/*")
    
    pisitools.removeDir("/usr/lib/python2.7/site-packages/tests")