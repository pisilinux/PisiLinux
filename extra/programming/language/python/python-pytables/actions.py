#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "tables-%s" % get.srcVERSION()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("doc/usersguide.pdf", "ANNOUNCE.txt", "LICENSE.txt", \
            "MIGRATING_TO_2.x.txt", "README.txt", "RELEASE_NOTES.txt", "THANKS")

    pisitools.insinto("%s/%s/examples" % (get.docDIR(), get.srcNAME()), "examples/*" )
    pisitools.insinto("%s/%s/scripts" % (get.docDIR(), get.srcNAME()), "doc/scripts/*.py" )
