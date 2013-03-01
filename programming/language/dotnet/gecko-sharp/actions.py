#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "gecko-sharp-2.0-%s" % get.srcVERSION()

def setup():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())

    autotools.configure()

def build():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())

    autotools.make()

def install():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "README*")
