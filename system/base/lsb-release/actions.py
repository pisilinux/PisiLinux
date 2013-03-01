#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def build():
    pisitools.dosed("Makefile", "prefix=.*", "prefix=%s" % get.defaultprefixDIR())
    autotools.make()

def install():
    autotools.install()

    pisitools.dodir("/etc")

    pisitools.dodoc("README", "ChangeLog")
