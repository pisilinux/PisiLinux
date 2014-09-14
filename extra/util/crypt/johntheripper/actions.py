#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "john-%s" % get.srcVERSION()

arch = "linux-x86-64" if get.ARCH() == "x86_64" else "linux-x86-sse2"

conf = {"CC": get.CC(),
        "CXX": get.CXX(),
        "CFLAGS": get.CFLAGS(),
        "LDFLAGS": get.LDFLAGS(),
        "ARCH": arch}
        # "CFLAGS": "%s -fno-PIC -fno-PIE" % get.CFLAGS(),
        # "LDFLAGS": "%s -nopie" % get.LDFLAGS(),

def setup():
    pisitools.dosed("src/params.h", '#define.*JOHN_SYSTEMWIDE_HOME.*"/usr/share/john"', '#define JOHN_SYSTEMWIDE_HOME "/etc/john"')

def build():
    shelltools.cd("src")
    autotools.make('CPP=%(CXX)s \
                    CC=%(CC)s \
                    AS=%(CC)s \
                    LD=%(CC)s \
                    CFLAGS="-c -Wall %(CFLAGS)s -DJOHN_SYSTEMWIDE" \
                    LDFLAGS="%(LDFLAGS)s" \
                    OPT_NORMAL="" \
                    %(ARCH)s' % conf)
                    # CFLAGS="-c -Wall %(CFLAGS)s -DJOHN_SYSTEMWIDE -DJOHN_SYSTEMWIDE_HOME=\\\"\\\\\\\"/etc/john\\\\\\\"\\\"" \

def install():
    pisitools.dosbin("run/john")
    pisitools.insinto("/usr/sbin", "run/mailer", "john-mailer")

    for f in ["unafs", "unique", "unshadow", "undrop"]:
        pisitools.dosym("john", "/usr/sbin/%s" % f)

    for f in ["john.conf", "password.lst", "*chr"]:
        pisitools.insinto("/etc/john", "run/%s" % f)

    pisitools.dodoc("doc/*")
