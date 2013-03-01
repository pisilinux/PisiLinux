#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "nose-%s" % get.srcVERSION()

examples = "%s/%s/" % (get.docDIR(), get.srcNAME())

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

def install():
    pisitools.dosed("setup.py", "man/man1", "share/man/man1")

    pythonmodules.install()

    pisitools.dohtml("doc/*")

    shelltools.chmod("examples/*", 0644)
    pisitools.insinto(examples, "examples/*")
