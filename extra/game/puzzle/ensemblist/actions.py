#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ensemblist-%s" % get.srcVERSION().split(".")[1]

def setup():
    shelltools.chmod("datas", 0755)
    shelltools.chmod("datas/*", 0644)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.doman("ensemblist.6")
    pisitools.dodoc("Changelog", "README")
