#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# this package needs a lot of work for init scripts etc.
def setup():
    autotools.configure("--enable-pthread \
                         --enable-password-save \
                         --enable-iproute2 \
                         --enable-ssl \
                         --enable-crypto \
                         --with-ifconfig-path=/sbin/ifconfig \
                         --with-iproute-path=/sbin/ip \
                         --with-route-path=/sbin/route")

def build():
    autotools.make()

    for d in ("plugin/auth-pam", "plugin/down-root", "easy-rsa/2.0"):
        autotools.make("-C %s" % d)

def check():
    shelltools.system("./openvpn-test.sh")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C easy-rsa/2.0 DESTDIR=%s/usr/share/%s/easy-rsa" % (get.installDIR(), get.srcNAME()))

    for val in ["auth-pam", "down-root"]:
        pisitools.dolib_so("plugin/%s/openvpn-%s.so" % (val, val), "/usr/lib/openvpn/plugin/lib/openvpn-%s.so" % val)

    for val in ["contrib", "sample-config-files", "sample-keys", "sample-scripts"]:
        pisitools.insinto("/%s/openvpn/%s" % (get.dataDIR(), val), "%s/*" % val)

    pisitools.dodir("/etc/openvpn")
    pisitools.dodir("/run/openvpn")
    pisitools.domove("/usr/share/openvpn/sample-config-files/server.conf", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample-config-files/client.conf", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample-config-files/firewall.sh", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample-config-files/xinetd-server-config", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample-config-files/xinetd-client-config", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample-config-files/loopback-server", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample-config-files/loopback-client", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample-config-files/openvpn-startup.sh", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample-config-files/openvpn-shutdown.sh", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample-keys/*.key", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample-keys/*.crt", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample-keys/*.pem", "/etc/openvpn")

     
    pisitools.dodoc("AUTHORS", "COPYING", "COPYRIGHT.GPL", "ChangeLog", "README")

