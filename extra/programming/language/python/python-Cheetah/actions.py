#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "Cheetah-%s" % get.srcVERSION()

def install():
    shelltools.export("CHEETAH_USE_SETUPTOOLS", "")
    pythonmodules.install()

    pisitools.dodoc("CHANGES", "TODO")
