#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "quesoglc-%s" % get.srcVERSION().split("_", 1)[0]

def setup():
    # make sure system fribidi is used
    shelltools.unlinkDir("src/fribidi")

    shelltools.touch("NEWS")
    autotools.autoreconf("-vfi")

    # allow glewx usage
    autotools.configure("--disable-dependency-tracking \
                         --disable-executables \
                         --disable-static \
                         --without-doc \
                         --with-fribidi \
                         --without-glew")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "THANKS")
    pisitools.insinto("/%s/%s/examples/" % (get.docDIR(), get.srcNAME()), "examples/*.c")
