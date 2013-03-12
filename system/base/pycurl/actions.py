#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    # no static libs
    pisitools.dosed("setup.py", ", \"--static-libs\"")

    pythonmodules.install()

    pisitools.removeDir("/usr/share/doc")

    pisitools.dodoc("ChangeLog", "COPYING*", "README", "TODO")
