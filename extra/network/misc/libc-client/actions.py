#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/osdep/unix/Makefile","SSLDIR=/usr/local/ssl","SSLDIR=/usr/")
    pisitools.dosed("src/osdep/unix/Makefile","SSLCERTS=$(SSLDIR)/certs","SSLCERTS=/etc/pki/tls/certs/")

def build():
    autotools.make("lnp EXTRAAUTHENTICATORS=gss SSLTYPE=unix.nopwd  \
            EXTRACFLAGS=\"%s\" " %get.CFLAGS())

def install():
    pisitools.dolib("c-client/libc-client.so.1.0.0")
    pisitools.dosym("/usr/lib/libc-client.so.1.0.0", "/usr/lib/libc-client.so.1")
    pisitools.dosym("libc-client.so.1.0.0","/usr/lib/libc-client.so")
    pisitools.dodir("/usr/include/imap")
    pisitools.insinto("/usr/include/imap", "src/c-client/*.h")
    pisitools.insinto("/usr/include/imap", "c-client/linkage.c")
    pisitools.insinto("/usr/include/imap", "c-client/linkage.h")
    pisitools.insinto("/usr/include/imap", "c-client/osdep.h")
    pisitools.insinto("/usr/include/imap", "src/osdep/unix/dummy.h")
    pisitools.insinto("/usr/include/imap", "src/osdep/unix/env_unix.h")
    pisitools.insinto("/usr/include/imap", "src/osdep/unix/f*.h")
    pisitools.insinto("/usr/include/imap", "src/osdep/unix/pseudo.h")
    pisitools.insinto("/usr/include/imap", "src/osdep/unix/tcp_unix.h")
    pisitools.insinto("/usr/include/imap", "src/osdep/unix/unix.h")
    pisitools.insinto("/usr/include/imap", "src/osdep/unix/os_slx.h")
    #pisitools.remove("/usr/include/imap/os_*.h")
