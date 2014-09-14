#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.rawConfigure()

def build():
    autotools.make("-j1")

def install():
    pisitools.insinto("/usr/lib/psi/plugins", "gstprovider/libgstprovider.so")

    pisitools.dodoc("COPYING", "README", "TODO")
