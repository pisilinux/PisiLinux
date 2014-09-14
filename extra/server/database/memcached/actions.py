#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure.ac", "-Werror")
    shelltools.system("touch README")
    autotools.autoreconf("-vfi")
    autotools.configure("%s" % ("--enable-64bit" if get.ARCH() == "x86_64" else ""))

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodir("/run/memcached")
    shelltools.chown("%s/run/memcached" % get.installDIR(), "memcached", "memcached")
    shelltools.chmod("%s/run/memcached" % get.installDIR())

    pisitools.dodoc("AUTHORS","README.md","NEWS","COPYING","doc/*.txt")
