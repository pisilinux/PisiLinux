#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # fix path
    pisitools.dosed("Makefile.in", "\$\(localstatedir\)(\/run\/)", "\\1")

    shelltools.system("./autogen.sh")

    pisitools.cflags.add("-D_GNU_SOURCE", "-DCTDB_VERS=\"%s\"" % get.srcVERSION())
    autotools.configure("--with-socketpath=/run/ctdb/ctdbd.socket")

def build():
    autotools.make("showflags")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING","README","NEWS")
