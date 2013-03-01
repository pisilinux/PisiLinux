#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "pyao-%s" % get.srcVERSION()
examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def setup():
    shelltools.system("./config_unix.py")

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.dodoc("AUTHORS", "README", "COPYING")

    shelltools.chmod("test.py", 0644)
    pisitools.insinto(examples, "test.py")

