#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make("-j8")

def install():
    autotools.install()

    pisitools.dohtml("httrack-doc.html")

    pisitools.dodoc("AUTHORS", "README", "greetings.txt", "history.txt")
