#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile.in", "xmlto man", "xmlto --skip-validation man")
    autotools.configure("--with-udev-rules \
                         --disable-rpath")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s udevrulesdir=/lib/udev/rules.d udevhelperdir=/lib/udev" % get.installDIR())

    pisitools.dodir("/run/udev-configure-printer")

    pisitools.dodoc("README", "AUTHORS", "NEWS", "COPYING", "ChangeLog")
