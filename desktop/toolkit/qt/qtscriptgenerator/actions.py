#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="%s-src-%s" % (get.srcNAME(), get.srcVERSION())

def setup():
    shelltools.cd("generator")
    shelltools.system("qmake generator.pro")
    shelltools.cd("../qtbindings")
    shelltools.system("qmake qtbindings.pro")

def build():
    shelltools.cd("generator")
    autotools.make("-j1")
    shelltools.system("QTDIR=/usr/share/qt4 ./generator --include-paths='/usr/include'")

    shelltools.cd("../qtbindings")
    autotools.make("-j1")

def install():
    pisitools.insinto("/usr/lib/qt4/plugins/script", "plugins/script/*")
    pisitools.insinto("%s/qtscriptgenerator" % get.docDIR(), "doc/*")

    pisitools.dodoc("LICENSE*", "LGPL*")
