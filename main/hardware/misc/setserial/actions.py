#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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

