#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "tcp_wrappers_%s" % get.srcVERSION()

def setup():
    shelltools.chmod("Makefile", 0755)
    pisitools.dosed("Makefile", "@make", "@$(MAKE) ")
    pisitools.dosed("Makefile", "make;", "$(MAKE);")

def build():
    MINOR = "7"
    REL = "6"

    shelltools.export("PARDUS_CFLAGS", "%s" % get.CFLAGS())

    args = 'REAL_DAEMON_DIR=%s \
            PARDUS_OPT="-fPIC -DPIC -D_REENTRANT -DHAVE_STRERROR -DHAVE_WEAKSYMS -DINET6=1 -Dss_family=__ss_family -Dss_len=__ss_len" \
            MAJOR=0 MINOR=%s REL=%s' % ( get.sbinDIR(), MINOR, REL )

    autotools.make("%s config-check" % args)
    autotools.make('%s LDFLAGS="-pie %s" linux' % (args, get.LDFLAGS()))

def install():
    for app in ["tcpd","tcpdchk","tcpdmatch","safe_finger","try-from"]:
        pisitools.dosbin(app)

    pisitools.insinto("/usr/include", "tcpd.h")

    pisitools.dolib_a("libwrap.a")

    # FIXME: this seems not necessary anymore
    # pisitools.domove("libwrap.so", "libwrap.so.0.%s" % get.srcVERSION())
    pisitools.dolib_so("libwrap.so.0.%s" % get.srcVERSION(), "/lib")

    pisitools.dosym("/lib/libwrap.so.0.%s" % get.srcVERSION(), "/lib/libwrap.so.0")
    pisitools.dosym("/lib/libwrap.so.0", "/lib/libwrap.so")

    libtools.gen_usr_ldscript("libwrap.so")

    pisitools.dosym("hosts_access.5", "/usr/share/man/man5/hosts.allow.5")
    pisitools.dosym("hosts_access.5", "/usr/share/man/man5/hosts.deny.5")

    pisitools.doman("*.3", "*.5", "*.8")
    pisitools.dodoc("BLURB", "CHANGES", "DISCLAIMER", "README*")

