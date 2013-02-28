#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

slshdoc = "/%s/slsh" % get.docDIR()
slangdoc = "/%s/slang/" % get.docDIR()

def setup():
    autotools.configure("--sysconfdir=/etc")

def build():
    autotools.make("-j1 install_doc_dir=/%s/%s all" % (get.docDIR(), get.installDIR()))

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s INST_LIB_DIR=%s/usr/lib" % (get.installDIR(),get.installDIR()))

    pisitools.domove("%s/*" % slshdoc, "%s/" % slangdoc)
    pisitools.domove("%s/v2/*" % slangdoc, "%s/" % slangdoc)
    pisitools.removeDir("%s/v2" % slangdoc)
    pisitools.removeDir("%s" % slshdoc)

