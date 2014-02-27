#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # disable example compilation
    pisitools.dosed("Makefile.in", "(SUBDIRS.*)examples", "SUBDIRS = gtkgl")
    pisitools.dosed("Makefile.am", "(SUBDIRS.*)examples", "SUBDIRS = gtkgl")

    autotools.autoreconf("-vif")
    autotools.configure("--with-lib-GL \
                         --disable-static")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for i in ["*.c", "*.h", "*.lwo", "README"]:
        pisitools.insinto("%s/gtkglarea/examples" % get.docDIR(), "examples/%s" % i)

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*", "docs/*.txt")
