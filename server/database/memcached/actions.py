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
    pisitools.dosed("configure.ac", "-Werror")
    autotools.autoreconf("-vfi")
    autotools.configure("%s" % ("--enable-64bit" if get.ARCH() == "x86_64" else ""))

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodir("/var/run/memcached")
    shelltools.chown("%s/var/run/memcached" % get.installDIR(), "memcached", "memcached")
    shelltools.chmod("%s/var/run/memcached" % get.installDIR())

    pisitools.dodoc("AUTHORS", "README", "doc/*.txt")
