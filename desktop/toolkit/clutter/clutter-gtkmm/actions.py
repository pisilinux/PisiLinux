#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-dependency-tracking \
                         --enable-shared \
                         --disable-static")

    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for i in shelltools.ls("examples/events"):
        if i.endswith(".h") or i.endswith(".cc"):
            pisitools.insinto("/%s/%s/examples/" % (get.docDIR(), get.srcNAME()), "examples/events/%s" % i)

    #pisitools.removeDir("/usr/lib/clutter-gtkmm-0.9")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS", "examples/redhand.png")
