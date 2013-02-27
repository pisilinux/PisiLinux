#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("CC=%s LIBDIR=/usr/lib EXLDFLAGS= PROG_EXTRA=sensord user" % get.CC())

def install():
    autotools.rawInstall("PREFIX=/usr MANDIR=/%s PROG_EXTRA=sensord DESTDIR=%s user_install" % (get.manDIR(), get.installDIR()))

    # Drop static lib
    pisitools.remove("/usr/lib/libsensors.a")

    pisitools.dodir("/etc/sensors.d")

    # Install systemd service
    pisitools.insinto("/lib/systemd/system", "prog/init/lm_sensors.service")

    pisitools.dodoc("CHANGES", "CONTRIBUTORS", "README")
