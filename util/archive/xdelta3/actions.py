#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir="xdelta%s" % get.srcVERSION()

def build():
    autotools.make('CFLAGS="%s -Wno-deprecated" all xdelta3-decoder xdelta3-tools' % get.CFLAGS())
    pythonmodules.compile()

def install():
    for i in ["xdelta3", "xdelta3-decoder", "xdelta3-tools"]:
        pisitools.dobin("xdelta3")

    pythonmodules.install()

    pisitools.doman("*.1")
    pisitools.dodoc("COPYING", "README")

    shelltools.chmod("examples/*", 0644)
    pisitools.insinto("/%s/%s/examples/" % (get.docDIR(), get.srcNAME()), "examples/*")
