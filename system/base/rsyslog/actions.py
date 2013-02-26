#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", '%s -fpie -DSYSLOGD_PIDNAME=\\\"syslogd.pid\\\"' % get.CFLAGS())
    shelltools.export("LDFLAGS", "-pie -Wl,-z,relro -Wl,-z,now")

    autotools.configure("--disable-static \
                         --disable-mysql \
                         --disable-pgsql \
                         --disable-gssapi-krb5 \
                         --disable-relp \
                         --disable-gnutls \
                         --disable-testbench \
                         --sbindir=/sbin \
                         --with-systemdsystemunitdir=/lib/systemd/system \
                         --enable-mail \
                         --enable-imfile \
                         --enable-unlimited-select")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # remove empty dir
    pisitools.removeDir("/usr/bin")

    pisitools.dodoc("COPYING*", "README", "AUTHORS", "ChangeLog")
