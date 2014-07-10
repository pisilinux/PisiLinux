#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "playonlinux"
NoStrip = "/"

datadir = "/usr/share"

def install():
    installdir = get.installDIR()+ datadir
    pisitools.dodir(datadir)
    pisitools.dodir("%s/applications" % datadir)

    shelltools.copytree("%s/playonlinux" % get.workDIR(), "%s/" % installdir)

    pisitools.dobin("%s/playonlinux/playonlinux" % installdir)

    pisitools.domo("%s/playonlinux/lang/po/tr.po" % installdir, "tr", "pol.mo")

#    pisitools.domove("usr/share/locale/tr/LC_MESSAGES", "/usr/share/playonlinux/lang/locale/tr")

    pisitools.dodoc("%s/playonlinux/LICENCE" % installdir, "%s/playonlinux/CHANGELOG.*" % installdir)

    shelltools.move("%s/etc/PlayOnLinux.desktop" % (get.installDIR() + "/usr/share/playonlinux"), "%s/usr/share/applications/PlayOnLinux.desktop" % get.installDIR())

    shelltools.unlink("%s/usr/bin/playonlinux" % get.installDIR())

    shelltools.sym("%s/usr/share/playonlinux/playonlinux" % get.installDIR(), "%s/usr/bin/playonlinux" % get.installDIR() )
    
    pisitools.dosed("playonlinux", "python2.6 mainwindow.py", "python2.8 mainwindow.py")