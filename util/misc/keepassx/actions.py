#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import qt4
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()

    # Update Turkish translation
    shelltools.system("lrelease src/translations/keepassx-tr_TR.ts")
    pisitools.insinto("/usr/share/keepassx/i18n/", "src/translations/*tr*.qm")

    #Remove unused mime info
    pisitools.removeDir("/usr/share/mimelnk")

    pisitools.dodoc("changelog", "COPYING")
