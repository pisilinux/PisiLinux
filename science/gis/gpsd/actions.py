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
    shelltools.touch("%s/ChangeLog" % get.curDIR())
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static \
                         --disable-libQgpsmm \
                         --enable-dbus")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")


def build():
    autotools.make()

def install():
    autotools.install()

    # We're using conf.d instead of sysconfig
    pisitools.dosed("gpsd.hotplug.wrapper", "sysconfig\/", "conf.d/")

    # Install UDEV files
    pisitools.insinto("/lib/udev/rules.d", "gpsd.rules", "99-gpsd.rules")
    pisitools.dobin("gpsd.hotplug", "/lib/udev")
    pisitools.dobin("gpsd.hotplug.wrapper", "/lib/udev")

    # Fix permissions
    shelltools.chmod("%s/usr/lib/%s/site-packages/gps/gps.py" % (get.installDIR(), get.curPYTHON()))

    pisitools.dodoc("README", "TODO", "AUTHORS", "COPYING")
