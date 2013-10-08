#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # AM_BINRELOC missing, just ignore
    shelltools.system("echo 'AC_DEFUN([AM_BINRELOC], [])' > acinclude.m4")
    autotools.autoreconf("-fi")
    autotools.configure("--enable-popt \
                        --enable-libxml2 \
                        --enable-libxml2-reader \
                        --enable-ps \
                        --enable-tfm=2 \
                        --enable-builder-cache \
                        --enable-breaks \
                        --enable-boxml \
                        --sysconfdir=/etc \
                        --with-t1lib \
                        --enable-svg")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ANNOUNCEMENT", "AUTHORS", "BUGS", "ChangeLog",
                    "CONTRIBUTORS", "COPYING", "HISTORY", "LICENSE",
                    "README", "TODO")
