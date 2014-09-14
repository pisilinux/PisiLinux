#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    cflags = "%s -fPIC" % get.CFLAGS()
    shelltools.export("CFLAGS", cflags)

    autotools.configure("--disable-static")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall('DESTDIR=%s man1dir=/usr/share/man/man1' % get.installDIR())

    pisitools.dohtml("doc/*")
    pisitools.dodoc("Changes", "README")
