#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("CC=%s CFLAGS='%s'" % (get.CC(), get.CFLAGS()))

def install():
    autotools.rawInstall("DESTDIR=%s prefix=/%s install-bin install-man" % (get.installDIR(), get.defaultprefixDIR()))

    pisitools.dodoc("AUTHORS", "CHANGELOG", "LICENSE", "README")
