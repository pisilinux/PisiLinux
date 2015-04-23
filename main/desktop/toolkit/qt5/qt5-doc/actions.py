#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import get


WorkDir="qtdoc-opensource-src-5.4.1"

def setup():
    shelltools.export("QT5LINK", "/usr/share/doc/qt5/global")
    shelltools.system("qmake-qt5 QMAKE_DOCS='doc/config/qtdoc.qdocconf' qtdoc.pro")
    qt5.configure(projectfile='qtdoc.pro', parameters='QMAKE_DOCS=doc/config/qtdoc.qdocconf')

def build():
    qt5.make("docs")

def install():
    qt5.install()
    qt5.install("install_docs")
