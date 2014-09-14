#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "metamail-2.7"

def setup():
    autotools.autoreconf ("-vfi")
    shelltools.chmod("configure")

    autotools.configure()

def build():

    autotools.make()

def install():

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "CREDITS", "README")

    shelltools.unlink("man/mailcap.?")
    pisitools.doman("man/*", "debian/mimencode.1", "debian/mimeit.1")

