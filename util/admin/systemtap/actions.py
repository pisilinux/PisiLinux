#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure.ac", "-Werror")
    pisitools.dosed("Makefile.am", "-Werror")
    autotools.autoreconf("-vfi")
    # --enable-publican --with-publican-brand=common
    autotools.configure("--enable-grapher \
                         --enable-sqlite \
                         --enable-pie \
                         --disable-docs \
                         --disable-publican \
                         --disable-crash \
                         --disable-silent-rules \
                         --docdir=/%s/%s \
                         --without-rpm" % (get.docDIR(), get.srcNAME()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/cache/systemtap")
    pisitools.dodir("/var/run/systemtap")
    pisitools.dodir("/var/log/stap-server")
    pisitools.dodir("/etc/logrotate.d")
    pisitools.dodir("/etc/stap-server/conf.d")
    pisitools.dodir("/etc/systemtap/conf.d")
    pisitools.dodir("/etc/systemtap/script.d")

    pisitools.dobin("stap-prep")

    shelltools.copytree("testsuite", "%s/usr/share/systemtap" % get.installDIR())

    pisitools.insinto("/etc/logrotate.d", "initscript/logrotate.stap-server", "stap-server")
    pisitools.insinto("/etc/conf.d", "initscript/config.stap-server", "stap-server")
    pisitools.insinto("/etc/systemtap", "initscript/config.systemtap", "config")

    # Clean uprobes directory
    #autotools.make("-C %s/usr/share/systemtap/runtime/uprobes clean" % get.installDIR())

    pisitools.dodoc("COPYING", "HACKING", "INTERNALS", "initscript/README.*")
