#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # Don't build examples
    pisitools.dosed("Makefile.am", "^(SRC_SUBDIRS.*?) examples", r"\1")

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-werror \
                         --enable-largefile")

def build():
    autotools.make()

def check():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO", "NEWS")
