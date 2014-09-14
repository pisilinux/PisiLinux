#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #autotools.autoreconf("-fi")
    autotools.configure("--disable-doxygen \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/include", "src/include/smbios")

    # Symlink to /usr/sbin/DellWirelessCtl for the new HAL
    pisitools.dosym("/usr/sbin/smbios-wireless-ctl", "/usr/sbin/DellWirelessCtl")

    # Remove yum specific stuff
    pisitools.removeDir("/etc/yum")
    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/usr/lib/yum-plugins")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
