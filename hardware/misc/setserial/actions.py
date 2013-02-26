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

docdir = "%s/%s" % (get.docDIR(), get.srcNAME())

def setup():
    autotools.configure()

def build():
    autotools.make("setserial")

def install():
    pisitools.doman("setserial.8")
    pisitools.dobin("setserial", "/bin")

    pisitools.insinto("/etc", "serial.conf")
    pisitools.dodoc("README")
    pisitools.dodir("%s/txt" % docdir)
    pisitools.insinto("%s/txt" % docdir, "Documentation/*")

