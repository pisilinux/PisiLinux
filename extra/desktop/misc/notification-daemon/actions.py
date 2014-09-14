#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-fi")

    #workaround for: "error: po/Makefile.in.in was not created by intltoolize." error at the end of configure
    shelltools.system("intltoolize --force --copy --automake")

    autotools.configure("--disable-schemas-install \
                         --disable-static")

    shelltools.cd("notification-daemon-engine-nodoka-0.1.0")
    #autotools.autoreconf("-vfi")
    autotools.configure()

def build():
    autotools.make()
    autotools.make("-C notification-daemon-engine-nodoka-0.1.0")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C notification-daemon-engine-nodoka-0.1.0 DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
