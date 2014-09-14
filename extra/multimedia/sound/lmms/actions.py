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
    cmaketools.configure("-DWANT_SYSTEM_SR=TRUE \
                          -DWANT_CAPS=TRUE \
                          -DWANT_TAP=TRUE \
                          -DWANT_PORTAUDIO=FALSE \
                          -DWANT_SYSTEM_SR=TRUE \
                          -DWANT_STK=FALSE \
                          -DWANT_VST_NOWINE=FALSE")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall('DESTDIR="%s"' % get.installDIR())
    pisitools.dodoc("AUTHORS","COPYING","TODO","README")
