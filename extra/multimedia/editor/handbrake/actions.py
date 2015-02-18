#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    # Use Python 2
    shelltools.system("sed -i 's/python2/python/g'  gtk/src/Makefile.am")
    # Force use of gtk2
    shelltools.system("sed -i 's/PKG_CHECK_MODULES(Gtk3.*/use_gtk3=no/' gtk/configure.ac")
    shelltools.cd("gtk")
    pisitools.dosed("configure.ac", "AM_CONFIG_HEADER", "AC_CONFIG_HEADERS")
    pisitools.dosed("configure.ac", "AM_PROG_CC_STDC", "AC_PROG_CC")
    autotools.autoreconf("-fiv")
    shelltools.cd("..")
    shelltools.system("./configure --force \
		      --prefix=/usr \
		      --disable-gtk-update-checks \
		      --verbose")

                       

def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README.*")
