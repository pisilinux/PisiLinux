#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

import os

def setup():
    for root, dirs, files in os.walk("share"):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

    autotools.configure("--enable-simd \
                         --enable-binreloc \
                         --enable-binreloc-threads")

def build():
    autotools.make()

def install():
    pisitools.dobin("src/loosecannon")
    pisitools.insinto("/usr/share","share/loosecannon")

    pythonmodules.fixCompiledPy("/usr/share/loosecannon")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
