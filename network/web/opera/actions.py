#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

arch = "i386" if get.ARCH() == "i686" else "x86_64"

WorkDir =  get.ARCH()

def install():
    shelltools.cd(shelltools.ls("%s/%s" % (get.workDIR(), WorkDir))[0])
    shelltools.system("./install --prefix /usr --force --repackage %s/usr" % get.installDIR())

    pisitools.dosym("/usr/lib/browser-plugins/libflashplayer.so", "/usr/lib/opera/plugins/libflashplayer.so")
