#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.cflags.add('-fpie -DSYSLOGD_PIDNAME=\\"syslogd.pid\\"')
    pisitools.ldflags.add("-pie -Wl,-z,relro -Wl,-z,now")

    autotools.configure("\
                         --sbindir=/usr/bin \
                         --disable-gui \
                         --disable-mysql \
                         --disable-pgsql \
                         --disable-relp \
                         --disable-gnutls \
                         --disable-static \
                         --disable-rfc3195 \
                         --disable-omjournal \
                         --disable-testbench \
                         --disable-mmnormalize \
                         --disable-gssapi-krb5 \
                         --enable-mail \
                         --enable-uuid \
                         --enable-zlib \
                         --enable-imdiag \
                         --enable-imfile \
                         --enable-imptcp \
                         --enable-mmanon \
                         --enable-omprog \
                         --enable-mmaudit \
                         --enable-pmsnare \
                         --enable-impstats \
                         --enable-omstdout \
                         --enable-omuxsock \
                         --enable-largefile \
                         --enable-pmlastmsg \
                         --enable-mmjsonparse \
                         --enable-pmrfc3164sd \
                         --enable-pmcisconames \
                         --enable-sm_cust_bindcdr \
                         --enable-unlimited-select \
                         --enable-pmaixforwardedfrom \
                         --enable-cached-man-pages \
                        ")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "README", "AUTHORS", "ChangeLog")
