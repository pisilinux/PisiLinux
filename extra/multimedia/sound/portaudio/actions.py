#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "portaudio"

def setup():
    autotools.configure("--disable-static --prefix=/usr")

def build():
    autotools.make()


def install():
    autotools.rawInstall('DESTDIR="%s" libdir=/usr/lib' % get.installDIR())

    pisitools.insinto("/%s/%s" % (get.docDIR(), get.srcNAME()), "doc/html")
    pisitools.dodoc("LICENSE.txt", "README.txt")
