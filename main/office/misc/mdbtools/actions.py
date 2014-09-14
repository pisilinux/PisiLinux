#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", ""))

def setup():
    shelltools.unlink("acinclude.m4")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-gtk-doc \
                         --disable-static \
                         --enable-sql \
                         --with-unixodbc=/usr")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")


def check():
    autotools.make("check")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README", "TODO")
