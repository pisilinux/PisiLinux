#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "microcode_ctl-%s" % get.srcVERSION()

def build():
    autotools.make('CC="%s" CFLAGS="%s"' % (get.CC(), get.CFLAGS()))


def install():
    autotools.install("DESTDIR=%s PREFIX=/usr INSDIR=/sbin" % get.installDIR())

    # Remove lib/firmware directory
    # We get it from intel-ucode and amd-ucode packages.
    pisitools.removeDir("/lib/firmware")

    pisitools.dodoc("Changelog", "README")

