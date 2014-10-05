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
    shelltools.export("LIRC_CFLAGS", "-llirc_client")
    shelltools.export("LIRC_LDFLAGS", "-llirc_client")

    autotools.autoreconf("-fi")
    autotools.configure("--enable-vdr-keys")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

    pisitools.removeDir("/usr/share/doc/xitk")
