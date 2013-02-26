#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%(DESTINATION)s \
                          INSTALLDIR=%(DESTINATION)s/usr/bin \
                          MANDIR=%(DESTINATION)s/usr/share/man/man1 \
                          INCLUDEDIR=%(DESTINATION)s/usr/include \
                          LOCALEDIR=%(DESTINATION)s/usr/share/locale \
                          PKGCONFIGDIR=%(DESTINATION)s/usr/lib/pkgconfig" % {'DESTINATION': get.installDIR()})

    pisitools.dodoc("AUTHORS", "COPYING", "README", "ChangeLog", "NEWS")
