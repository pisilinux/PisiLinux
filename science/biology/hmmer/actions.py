#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

tutorial = "%s/%s/tutorial" % (get.docDIR(), get.srcNAME())

def setup():
    shelltools.chmod("tutorial/*", 0644)
    autotools.configure("--enable-threads")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYRIGHT", "LICENSE", "RELEASE-NOTES", "Userguide.pdf", )
    pisitools.insinto(tutorial, "tutorial/*")
