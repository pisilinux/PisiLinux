#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--prefix=/usr")

def build():
    autotools.make("run-parts")

def install():
    pisitools.dobin("run-parts")
    pisitools.doman("run-parts.8")
    
    pisitools.insinto("/usr/share/man/de/man8/", "po4a/de/run-parts.8")
    pisitools.insinto("/usr/share/man/es/man8/", "po4a/es/run-parts.8")
    pisitools.insinto("/usr/share/man/fr/man8/", "po4a/fr/run-parts.8")
    pisitools.insinto("/usr/share/man/it/man8/", "po4a/it/run-parts.8")
    pisitools.insinto("/usr/share/man/ja/man8/", "po4a/ja/run-parts.8")
    pisitools.insinto("/usr/share/man/pl/man8/", "po4a/pl/run-parts.8")
    pisitools.insinto("/usr/share/man/sl/man8/", "po4a/sl/run-parts.8")