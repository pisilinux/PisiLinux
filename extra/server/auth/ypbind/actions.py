#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ypbind-mt-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-dbus-nm")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\"" % get.installDIR())

    pisitools.insinto("/etc", "etc/yp.conf")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "THANKS", "TODO")
