#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "foomatic-filters-%s" % get.srcVERSION().replace("_", "-")

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-file-converter-check")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/bin/foomatic-rip", "/usr/lib/cups/filter/cupsomatic")
    pisitools.dosym("/usr/bin/foomatic-rip", "/usr/bin/lpdomatic")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "COPYING", "NEWS", "TODO", "USAGE")
