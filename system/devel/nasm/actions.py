#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "nasm-%s" % get.srcVERSION().replace("_", "")

binFiles = ["nasm", "ndisasm"]
rdoffFiles = ["ldrdf", "rdf2bin", "rdf2ihx", "rdfdump", "rdflib", "rdx"]

def setup():
    autotools.configure()

def build():
    autotools.make("all")
    autotools.make("rdf")

def install():
    for i in rdoffFiles:
        binFiles.append("rdoff/%s" % i)

    for i in binFiles:
        pisitools.dobin(i)

    pisitools.dosym("rdf2bin", "/usr/bin/rdf2com")

    pisitools.doman("nasm.1", "ndisasm.1")
    pisitools.dodoc("AUTHORS", "CHANGES", "ChangeLog", "README", "TODO", "doc/nasmdoc.*")
