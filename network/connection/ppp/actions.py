#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.cflags.add("-fPIC", "-D_GNU_SOURCE")
    shelltools.copytree("%s/dhcp" % get.workDIR(), "pppd/plugins")
    pisitools.dosed("pppd/plugins/dhcp/Makefile.linux", "^(CFLAGS=.+)\s-O2", "\\1 %s" % get.CFLAGS())

    # Enable atm
    pisitools.dosed("pppd/Makefile.linux", "^#(HAVE_LIBATM=yes)", "\\1")
    # Enable pam
    pisitools.dosed("pppd/Makefile.linux", "^#(USE_PAM=y)", "\\1")
    # Enable CBCP
    pisitools.dosed("pppd/Makefile.linux", "^#(CBCP=y)", "\\1")
    # Enable IPv6
    pisitools.dosed("pppd/Makefile.linux", "^#(HAVE_INET6)", "\\1")
    # Enable dhcp
    pisitools.dosed("pppd/plugins/Makefile.linux", "^(SUBDIRS\s:=.+)", "\\1 dhcp")

    autotools.configure()

def build():
    autotools.make()

def install():
    # The build mechanism is crap. Don't remove \/usr from DESTDIR or else the paths will fail
    autotools.rawInstall("DESTDIR=%s/usr INSTROOT=%s install-etcppp" % ((get.installDIR(),)*2))

    # No suid libraries
    shelltools.chmod("%s/usr/lib/pppd/%s/*.so" % (get.installDIR(),get.srcVERSION()), 0755)

    # Install Radius config files
    pisitools.insinto("/etc/radiusclient", "pppd/plugins/radius/etc/*")

    # Create peers directory
    pisitools.dodir("/run/ppp")
    pisitools.dodir("/etc/ppp/peers")

    pisitools.dodoc("Changes*", "README*", "FAQ")
