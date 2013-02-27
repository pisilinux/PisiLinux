#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="%s" % get.srcDIR().replace("_", "")

def setup():
    shelltools.export("CFLAGS", "%s -pie -fPIE -fno-strict-aliasing" % get.CFLAGS())

    # needed to link with avahi
    shelltools.export("ac_cv_header_dns_sd_h", "yes")
    shelltools.export("ac_cv_lib_dns_sd_DNSServiceRegister", "yes")

    pisitools.dosed("ntpstat-0.2/Makefile", "^CC=.*gcc", "CC=%s" % get.CC())
    pisitools.dosed("ntpstat-0.2/Makefile", "^CFLAGS=.*", "CFLAGS=%s" % get.CFLAGS())

    autotools.configure("--enable-all-clocks \
                         --enable-parse-clocks \
                         --enable-linuxcaps \
                         --enable-ipv6 \
                         --with-crypto")

def build():
    autotools.make()
    autotools.make("-C ntpstat-0.2")

    shelltools.cd("html")
    shelltools.system("../scripts/html2man")
    shelltools.system("../fix-man-pages")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove autotools installed man pages
    pisitools.removeDir("/usr/share/man")

    pisitools.doman("html/man/man5/*.5", "html/man/man8/*.8")

    for sbin in ["sntp", "ntpdc", "ntpd", "ntp-keygen", "ntp-wait",
                 "ntpq", "ntptime", "ntptrace", "tickadj", "ntpsnmpd", "ntpdate"]:
        pisitools.domove("/usr/bin/%s" % sbin, "/usr/sbin")

    # Additional ntpstat binary and man page
    pisitools.dobin("ntpstat-0.2/ntpstat")
    pisitools.doman("ntpstat-0.2/ntpstat.1")

    pisitools.dodir("/var/lib/ntp")

    pisitools.removeDir("/usr/lib")

    pisitools.dohtml("html/*")
    pisitools.dodoc("ChangeLog", "NEWS", "README", "TODO", "WHERE-TO-START")
