#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    # autotools.autoreconf("-vfi")
    autotools.configure('--disable-rpath \
                         --disable-static \
                         --disable-watchdog \
                         --disable-debugging \
                         --disable-optimization \
                         --docdir="/%s/%s" \
                         --enable-shared \
                         --enable-interfaces="c cxx" \
                         --with-pic' % (get.docDIR(), get.srcNAME()))
def build():
    autotools.make()

# tests run hours and hours, running it is left to packager
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("BUGS", "COPYING", "CREDITS", "ChangeLog", "STANDARDS", "TODO", "README*", "NEWS")
