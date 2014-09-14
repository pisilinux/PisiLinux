#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --with-x \
                         --with-ssl")

def configure():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s TERMINFO=%s/usr/share/terminfo" % (get.installDIR(),get.installDIR()))

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README*", "TODO", "linux/README")
