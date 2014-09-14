#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.configure("--with-lfs")

def build():
    autotools.make()

def install():
    pisitools.dobin("vobcopy")

    pisitools.doman("vobcopy.1")
    pisitools.dodoc("Changelog", "COPYING", "README")
