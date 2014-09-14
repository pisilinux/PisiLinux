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
    # We have a patch to use system gsm
    shelltools.unlinkDir("gsm")

    # Update gettext macros to be compatible with recent libtool
    shelltools.system("autopoint -f")

    # Remove missing to get an updated one
    shelltools.unlink("missing")

    autotools.autoreconf("-vif")
    autotools.configure("--disable-rpath")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "TODO")
