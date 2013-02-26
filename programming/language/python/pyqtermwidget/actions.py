# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.cd("pyqt4")
    shelltools.system("python config.py")

def build():
    shelltools.cd("pyqt4")
    autotools.make()

def install():
    shelltools.cd("pyqt4")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README")

