#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s man_prefix=/usr/share/man" % get.installDIR())
    pisitools.insinto("/etc", "src/config/hosts.atm")

    pisitools.dodoc("AUTHORS", "THANKS", "ChangeLog", "BUGS", "NEWS", "README")
