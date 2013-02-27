#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure", "HAVE_PYTHON=yes", "HAVE_PYTHON=no")
    autotools.configure("--enable-static=no")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "examples")
