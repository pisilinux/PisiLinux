#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    # Remove binary translations
    shelltools.unlink("translations/*.qm")
    shelltools.system("qmake %s.pro" % get.srcNAME())

def build():
    autotools.make()
    shelltools.cd("translations")
    shelltools.system("lrelease *.ts")

def install():
    pisitools.dobin("fet")
    pisitools.doman("doc/fet.1")
    pisitools.insinto("/usr/share/%s/translations" % get.srcNAME(), "translations/*.qm")

    # Install examples
    pisitools.insinto("/usr/share/%s/examples" % get.srcNAME(), "examples/*")

    pisitools.dodoc("ChangeLog", "COPYING", "README", "REFERENCES")
