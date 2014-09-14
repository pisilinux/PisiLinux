#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#
# Note : Gentoo ebuild also processes the hiscore.dat file which is not included
# in the default Makefile but is present in the source tree. Since Pisi Linux does not
# have a global hiscore directory no such action is taken. Each user will have his/her
# own hiscore table in the relevant home directory.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip = "/"
WorkDir = "njam-1.25-src"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dohtml("html/")
    pisitools.removeDir("/usr/share/njam/html")
    pisitools.dodoc("TODO", "COPYING", "README", "AUTHORS")
