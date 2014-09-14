#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("ChangeLog", "README", "THANKS")

    pythonmodules.fixCompiledPy("/usr/share/kde4/apps/frescobaldi/lib/frescobaldi_app") 
    pythonmodules.fixCompiledPy("/usr/share/kde4/apps/frescobaldi/lib")