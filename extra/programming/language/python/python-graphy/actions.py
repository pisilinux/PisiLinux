#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.insinto("/usr/lib/python2.7/site-packages/", "graphy")
    pisitools.insinto("/usr/share/doc/python-graphy/", "examples")

    # Copy examples
    pisitools.insinto("/usr/share/doc/python-graphy/", "README")