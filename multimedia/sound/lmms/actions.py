#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DWANT_SYSTEM_SR=TRUE \
                          -DWANT_CAPS=TRUE \
                          -DWANT_TAP=TRUE \
                          -DWANT_PORTAUDIO=FALSE \
                          -DWANT_SYSTEM_SR=TRUE \
                          -DWANT_STK=FALSE \
                          -DWANT_VST_NOWINE=FALSE", sourceDir="..")

def build():
    shelltools.cd("build")

    cmaketools.make()

def install():
    shelltools.cd("build")

    cmaketools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # pisitools.dosym("/usr/share/lmms/themes/default/icon.png", "/usr/share/pixmaps/lmms.png")

    pisitools.dodoc("../AUTHORS", "../COPYING", "../TODO", "../README")
