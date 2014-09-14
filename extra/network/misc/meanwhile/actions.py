# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--enable-doxygen=no \
                         --enable-static=no \
                         --disable-mailme")

def build():
    autotools.make()

def install():
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.install()

    pisitools.dodoc("README", "ChangeLog", "AUTHORS", "COPYING", "LICENSE", "TODO")
