#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "tuxpaint-stamps-2009.06.28"

def install():
    pisitools.dodoc("docs/*.txt")
    docdir = "%s/%s" % (get.docDIR(), get.srcNAME())
    shelltools.copytree("docs/el", "%s/%s/" % (get.installDIR(), docdir))
    shelltools.copytree("docs/es", "%s/%s/" % (get.installDIR(), docdir))
    shelltools.copytree("docs/fr", "%s/%s/" % (get.installDIR(), docdir))
    shelltools.copytree("docs/hu", "%s/%s/" % (get.installDIR(), docdir))
    autotools.make("install-all PREFIX=%s/usr" % get.installDIR())


