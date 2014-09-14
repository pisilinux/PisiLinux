#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    cmaketools.configure("-DNOSERVER=1")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "QTfrontend/res/teamicon.png", "hedgewars.png")
    #shelltools.system("lrelease-qt4 share/hedgewars/Data/Locale/hedgewars_tr_TR.ts -qm %s/usr/share/hedgewars/Data/Locale/hedgewars_tr_TR.qm" % get.installDIR())

    pisitools.doman("man/hedgewars.6")

    pisitools.dodoc("COPYING", "README", "Fonts_LICENSE.txt")