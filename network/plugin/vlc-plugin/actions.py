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

def setup():
    autotools.configure("--disable-silent-rules")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/lib/mozilla/plugins/*", "/usr/lib/browser-plugins")
    pisitools.removeDir("/usr/lib/mozilla/")

    pisitools.dodoc("AUTHORS", "NEWS", "README", "COPYING")

