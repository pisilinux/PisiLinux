#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

cpuparameter = "" if get.ARCH() == "x86_64" else "--enable-mmx"

def setup():
    autotools.configure("--disable-static \
                         %s" % cpuparameter)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "license.txt", "NEWS", "README", "doc/*.txt")
