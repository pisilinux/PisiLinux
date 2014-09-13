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
                         --disable-examples \
                         --with-x \
                         --program-suffix=2")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # FIXME: enable it when we swich to libusb 1.0
    #pisitools.removeDir("/usr/share/man/man3")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
