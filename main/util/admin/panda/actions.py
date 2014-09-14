#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def setup():
    # remove pae modules
    pisitools.dosed("panda.py", "-pae-", deleteLine=True)

    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc('AUTHORS', 'COPYING', 'README')
