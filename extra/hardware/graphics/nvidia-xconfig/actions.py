#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def build():
    autotools.make("STRIP_CMD=/bin/true")

def install():
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr" % get.installDIR())
    pisitools.dodoc("COPYING")
