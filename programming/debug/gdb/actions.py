#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "gdb-%s" % get.srcVERSION().replace("_", ".")

def setup():
    pisitools.dosed("configure", "^ppl_minor_version=10", "ppl_minor_version=11")
    pisitools.dosed("configure.ac", "^ppl_minor_version=10", "ppl_minor_version=11")
    pisitools.dosed("config/override.m4", "2.64", "2.69")

    autotools.autoreconf("-vfi")
    autotools.configure("--with-system-readline \
                         --with-separate-debug-dir=/usr/lib/debug \
                         --with-gdb-datadir=/usr/share/gdb \
                         --with-pythondir=/usr/lib/%s/site-packages \
                         --enable-tui \
                         --disable-nls \
                         --disable-sim \
                         --disable-rpath \
                         --disable-werror \
                         --without-rpm \
                         --with-python \
                         --with-expat" % get.curPYTHON())


def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # These come from binutils
    pisitools.removeDir("/usr/include")

    for f in shelltools.ls("%s/usr/lib/" % get.installDIR()):
        if shelltools.isFile("%s/usr/lib/%s" % (get.installDIR(), f)):
            pisitools.remove("/usr/lib/%s" % f)

    # these are not necessary
    for info in ["bfd","configure","standards"]:
        pisitools.remove("/usr/share/info/%s.info" % info)

    pisitools.dodoc("README*", "MAINTAINERS", "COPYING*", "ChangeLog*")
