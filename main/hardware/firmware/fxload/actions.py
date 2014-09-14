#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "fxload-2008_10_13"

def build():
    autotools.make("RPM_OPT_FLAGS=\"%s\"" % get.CFLAGS())

def install():
    autotools.rawInstall("prefix=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README.txt")
