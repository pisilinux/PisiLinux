#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mt-st-%s" % get.srcVERSION()

def build():
    autotools.make("CC=%s RPM_OPT_FLAGS=\"%s\"" % (get.CC(), get.CFLAGS()))

def install():
    autotools.install("RPM_BUILD_ROOT=%s" % get.installDIR())

    pisitools.dodoc("stinit.def.examples", "README*")
