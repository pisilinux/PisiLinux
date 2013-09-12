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
    # Fix pppoe and pppol2tp build problems
    shelltools.unlink("include/linux/if_pppol2tp.h")

    autotools.configure()

def build():
    autotools.make("CC=%s RPM_OPT_FLAGS='%s -fPIC'" % (get.CC(), get.CFLAGS()))

def install():
    # The build mechanism is crap. Don't remove \/usr from DESTDIR or else the paths will fail
    autotools.rawInstall("DESTDIR=%s/usr INSTROOT=%s install-etcppp" % ((get.installDIR(),)*2))

    # No suid libraries
    shelltools.chmod("%s/usr/lib/pppd/%s/*.so" % (get.installDIR(),get.srcVERSION()), 0755)

    # Install Radius config files
    pisitools.insinto("/etc/radiusclient", "pppd/plugins/radius/etc/*")

    # Remove unused directory, the log file is at /var/log/ppp.log
    pisitools.removeDir("/var")

    # Create peers directory
    pisitools.dodir("/run/ppp")
    pisitools.dodir("/etc/ppp/peers")

    pisitools.dodoc("Changes*", "README*", "FAQ")
