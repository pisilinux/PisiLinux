#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def install():
    pythonmodules.install()
    pisitools.insinto(examples, "*.py")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("LICENSE", "README*")
