#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4
from pisi.actionsapi import get

WorkDir = "%s-Source" % get.srcDIR()

shelltools.export("LDFLAGS", "")

def setup():
    cmaketools.configure()

    shelltools.cd("src/gui")
    qt4.configure()

def build():
    cmaketools.make()

    shelltools.cd("src/gui")
    qt4.make()

def install():
    pisitools.dobin("bin/synergyc")
    pisitools.dobin("bin/synergys")
    pisitools.dobin("bin/qsynergy")

    shelltools.chmod("%s/doc/*" % get.curDIR(), 0644)
    shelltools.chmod("%s/res/*" % get.curDIR(), 0644)

    pisitools.insinto("/etc","doc/synergy.conf.example", "synergy.conf")

    pisitools.insinto("/usr/share/applications", "res/synergy.desktop")
    pisitools.insinto("/usr/share/pixmaps", "res/synergy.ico")

    pisitools.insinto("/usr/share/man/man8", "doc/synergyc.man", "synergyc.8")
    pisitools.insinto("/usr/share/man/man8", "doc/synergys.man", "synergys.8")

    # Adding Mac stuff because some Pardus users may have Mac OS X too
    pisitools.dodoc("ChangeLog", "COPYING", "README", "doc/MacReadme.txt", "doc/org.synergy-foss.org*", "doc/synergy.conf*")
