#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt4
from pisi.actionsapi import get

WorkDir = "qt-assistant-qassistantclient-library-compat-version-%s" % get.srcVERSION()

def setup():
    qt4.configure(parameters='QT_PRODUCT=OpenSource')

def build():
    qt4.make()

    shelltools.cd("lib")
    qt4.configure(parameters='CONFIG=create_prl')
    qt4.make()

    shelltools.cd("../translations")
    shelltools.system("lrelease assistant_adp_*.ts")


def install():
    qt4.install()

    qt4.install("-C lib")

    pisitools.insinto("/usr/share/qt4/mkspecs/features/", "features/assistant.prf")

    pisitools.dodir("/usr/share/qt4/translations")
    pisitools.insinto("/usr/share/qt4/translations", "translations/*qm")

    pisitools.dodoc("LICENSE*", "LGPL*")
