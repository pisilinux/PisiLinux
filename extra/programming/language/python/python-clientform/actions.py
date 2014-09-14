#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ClientForm-%s" % get.srcVERSION()

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME()) 

def install():
    pythonmodules.install()

    pisitools.dodoc("ChangeLog.txt", "COPYING.txt", "README.txt")
    pisitools.dohtml("GeneralFAQ.html")
    pisitools.remove("/usr/share/doc/python-clientform/README.html.in")

    shelltools.chmod("examples/*", 0644)
    pisitools.insinto(examples, "examples/*") 

