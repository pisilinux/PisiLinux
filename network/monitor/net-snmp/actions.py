#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

MIBS = "host agentx smux \
       ucd-snmp/diskio tcp-mib udp-mib mibII/mta_sendmail \
       ip-mib/ipv4InterfaceTable ip-mib/ipv6InterfaceTable \
       ip-mib/ipAddressPrefixTable/ipAddressPrefixTable \
       ip-mib/ipDefaultRouterTable/ipDefaultRouterTable \
       ip-mib/ipv6ScopeZoneIndexTable ip-mib/ipIfStatsTable \
       sctp-mib rmon-mib etherlike-mib"

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure('--enable-shared \
                         --disable-static \
                         --without-rpm \
                         --with-sys-location=Unknown \
                         --with-sys-contact=root@Unknown \
                         --with-default-snmp-version=3 \
                         --with-logfile=/var/log/snmpd.log \
                         --with-persistent-directory=/var/lib/net-snmp \
                         --with-mib-modules="%s" \
                         --enable-ipv6 \
                         --enable-ucd-snmp-compatibility \
                         --with-openssl \
                         --with-pic \
                         --enable-embedded-perl \
                         --with-libwrap \
                         --enable-as-needed \
                         --without-root-access \
                         --enable-mfd-rewrites \
                         --with-temp-file-pattern="/run/net-snmp/snmp-tmp-XXXXXX" \
                         --enable-local-smux' % MIBS)
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-j1")

    shelltools.cd("python")
    pythonmodules.compile("--basedir=..")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("python")
    pythonmodules.install('--skip-build --basedir=..')
    shelltools.cd("..")

    pisitools.insinto("/etc/snmp/", "EXAMPLE.conf", "snmpd.conf.example")

    pisitools.dodir("/var/lib/net-snmp")
    pisitools.dodir("/etc/snmp")

    pisitools.dodoc("AGENT.txt", "ChangeLog", "FAQ", "NEWS", "PORTING", "README", "TODO")

    perlmodules.removePacklist()
    perlmodules.removePodfiles()
