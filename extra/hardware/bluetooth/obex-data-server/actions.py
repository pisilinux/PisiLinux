#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-bip=magick")

def build():
    autotools.make()

def install():
    shelltools.chmod("test/*py")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "COPYING", "dbus-api.txt", "test/ods-dbus-test.c", "test/ods-server-test.py",
                    "test/ods-session-test.py")
