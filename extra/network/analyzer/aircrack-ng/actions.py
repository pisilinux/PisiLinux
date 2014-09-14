#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("sqlite=true")

def install():
    autotools.install("sqlite=true mandir=%s/usr/share/man/man1" % get.installDIR())

    pisitools.insinto("/usr/share/aircrack-ng-%s" % get.srcVERSION(), "test/*")

    pisitools.dodoc("ChangeLog", "README", "AUTHORS")
