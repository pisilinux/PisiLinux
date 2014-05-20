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
    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE -fPIC" % get.CFLAGS())
#in some troff man pages
    #for i in ["dhclient.conf.5", "dhclient.leases.5", "dhclient-script.8", "dhclient.8"]:
    #    pisitools.dosed("client/%s" % i, "CLIENTBINDIR", "/sbin")
    #   pisitools.dosed("client/%s" % i, "RUNDIR", "/run")
    #  pisitools.dosed("client/%s" % i, "DBDIR", "/var/lib/dhcpd")
    # pisitools.dosed("client/%s" % i, "ETCDIR", "/etc/dhcp")

    #for i in ["dhcpd.conf.5", "dhcpd.leases.5", "dhcpd.8"]:
    #    pisitools.dosed("server/%s" % i, "CLIENTBINDIR", "/sbin")
    #   pisitools.dosed("server/%s" % i, "RUNDIR", "/run")
    #    pisitools.dosed("server/%s" % i, "DBDIR", "/var/lib/dhcpd")
    #   pisitools.dosed("server/%s" % i, "ETCDIR", "/etc/dhcp")

    pisitools.dosed("client/scripts/linux", "/etc/dhclient-exit-hooks", "/etc/dhcp/dhclient-exit-hooks")
    pisitools.dosed("client/scripts/linux", "/etc/dhclient-enter-hooks", "/etc/dhcp/dhclient-enter-hooks")

    autotools.autoreconf("-vfi")
    autotools.configure("--with-srv-lease-file=/var/lib/dhcpd/dhcpd.leases \
                         --with-srv6-lease-file=/var/lib/dhcpd/dhcpd6.leases \
                         --with-cli-lease-file=/var/lib/dhclient/dhclient.leases \
                         --with-cli6-lease-file=/var/lib/dhclient/dhclient6.leases \
                         --with-srv-pid-file=/run/dhcpd.pid \
                         --with-srv6-pid-file=/run/dhcpd6.pid \
                         --with-cli-pid-file=/run/dhclient.pid \
                         --with-cli6-pid-file=/run/dhclient6.pid \
                         --with-relay-pid-file=/run/dhcrelay.pid \
                         --with-ldap \
                         --with-ldapcrypto")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove files we don't want
    pisitools.remove("/etc/dhcpd.conf.example")
    pisitools.remove("/etc/dhclient.conf.example")

    # Install dhcp.schema for LDAP configuration
    pisitools.insinto("/etc/openldap/schema", "contrib/ldap/dhcp.schema")

    # dhclient configuration per service support is not ready yet, no need to create this directory for now
    # Install empty directory for dhclient.d scripts
    #pisitools.dodir("/etc/dhcp/dhclient.d")

    # Create directory hierarchy in /var
    pisitools.dodir("/var/lib/dhcpd")
    pisitools.dodir("/var/lib/dhclient")

    # Sample configuration files
    pisitools.insinto("/usr/share/doc/dhcp", "client/dhclient.conf.5", "dhclient.conf.exsample")
    pisitools.insinto("/usr/share/doc/dhcp", "server/dhcpd.conf.5", "dhcpd.conf.example")
    pisitools.insinto("/usr/share/doc/dhcp", "doc/examples/dhclient-dhcpv6.conf")
    pisitools.insinto("/usr/share/doc/dhcp", "doc/examples/dhcpd-dhcpv6.conf")

    pisitools.dodoc("LICENSE", "README", "RELNOTES")
