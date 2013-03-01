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
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --with-cd-paranoia-name=libcdio-paranoia \
                         --disable-rpath")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % (get.installDIR()))

    pkgconfig = ["libcdio_paranoia.pc","libcdio_cdda.pc",\
                 "libiso9660++.pc","libcdio++.pc"]
    for file in pkgconfig:
        pisitools.insinto("/usr/lib/pkgconfig",file)

    shelltools.chmod("%s/usr/lib/*" % get.installDIR(), 0644)

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS")
