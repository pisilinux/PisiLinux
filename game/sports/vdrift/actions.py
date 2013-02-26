#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import get

version = get.srcVERSION().split("_", 1)[1]
WorkDir = "vdrift-%s-%s-%s" % (version[0:4], version[4:6], version[6:])

#def setup():
    # shelltools.export("CXXFLAGS", get.CXXFLAGS())
    # shelltools.cd("bullet-2.66")
    # shelltools.system("./configure")
    # shelltools.system("jam bulletcollision bulletmath")
    # FIXME: BSG ???
    #shelltools.system("tar zxvf bullet-2.73-sp1.tgz")


def build():
    # shelltools.export("CXXFLAGS", get.CXXFLAGS())


    scons.make('release=1 \
                destdir="%s" \
                prefix=/usr \
                datadir=share/vdrift \
                bindir=bin \
                localedir=share/locale \
                os_cc=1 \
                os_cxx=1 \
                os_cxxflags=1 \
                use_binreloc=0' % get.installDIR())


def install():
    pisitools.dobin("build/vdrift")

    pisitools.dodoc("docs/AUTHORS", "docs/ChangeLog", "docs/COPYING", "docs/NEWS", "docs/README", "docs/TODO", "docs/VAMOS.txt")


