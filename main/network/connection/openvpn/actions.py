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
#pisitools.cflags.add("-DPLUGIN_LIBDIR=\\\"/usr/lib/openvpn\\\"")
#shelltools.export("CFLAGS", "%s -DPLUGIN_LIBDIR=\\\"/usr/lib/openvpn\\\"" % get.CFLAGS())
def setup():
    autotools.configure("--prefix=/usr \
                         --enable-password-save \
                         --enable-iproute2 \
                         --enable-ssl \
                         --enable-crypto \
                         --mandir=/usr/share/man \
                         --sbindir=/usr/bin")
#
def build():
    autotools.make()
    shelltools.cd("src/plugins/auth-pam")
    autotools.make()
    shelltools.cd("../down-root/")
    autotools.make
    shelltools.cd("..")
def check():
    shelltools.system("./openvpn-test.sh")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for val in ["contrib", "sample/sample-config-files", "sample/sample-keys", "sample/sample-scripts"]:
        pisitools.insinto("/%s/openvpn/%s" % (get.dataDIR(), val), "%s/*" % val)

    pisitools.dodir("/etc/openvpn")
    pisitools.dodir("/run/openvpn")
    pisitools.domove("/usr/share/openvpn/sample/sample-config-files/server.conf", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample/sample-config-files/client.conf", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample/sample-config-files/firewall.sh", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample/sample-config-files/xinetd-server-config", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample/sample-config-files/xinetd-client-config", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample/sample-config-files/loopback-server", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample/sample-config-files/loopback-client", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample/sample-config-files/openvpn-startup.sh", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample/sample-config-files/openvpn-shutdown.sh", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample/sample-keys/*.key", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample/sample-keys/*.crt", "/etc/openvpn")
    pisitools.domove("/usr/share/openvpn/sample/sample-keys/*.pem", "/etc/openvpn")


    pisitools.dodoc("AUTHORS", "COPYING", "COPYRIGHT.GPL", "ChangeLog", "README")

