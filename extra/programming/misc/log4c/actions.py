#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --disable-doc \
                         --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/include", "src/log4c.h")

    # Move the example config file to docdir
    pisitools.domove("/etc/log4crc.sample", "/%s/log4c" % get.docDIR())
    pisitools.removeDir("/etc")

    pisitools.dodoc("README", "AUTHORS", "COPYING", "ChangeLog", "TODO", "NEWS")
