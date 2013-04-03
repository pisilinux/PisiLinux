#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())
NoStrip=["/usr/share"]

def setup():
    kde4.configure("-DWITH_JINGLE=TRUE -DMOZPLUGIN_INSTALL_DIR=/usr/lib/browser-plugins \
                    -DWITH_Xmms=OFF \
                    -DWITH_LibMeanwhile=OFF \
                    -DWITH_qq=OFF")

def build():
    kde4.make()

def install():
    kde4.install()
