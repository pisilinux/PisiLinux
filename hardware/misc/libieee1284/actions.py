#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static")

def configure():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "NEWS", "TODO", "README", "doc/interface*")
