#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure()
    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    shelltools.export("MONO_SHARED_DIR",".")
    shelltools.export("LC_ALL","C")
    autotools.make()

def install():
    shelltools.export("MONO_SHARED_DIR",".")
    shelltools.export("MONO_GAC_PREFIX","%s/usr/lib" % get.installDIR())
    shelltools.export("GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL", "1")

    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "HACKING", "NEWS", "README")
