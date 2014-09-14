#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

def build():
    scons.make("PREFIX=/usr FAKE_ROOT=%s" % get.installDIR())

def install():
    scons.install()

    pisitools.dosym("/usr/share/linuxdcpp/pixmaps/linuxdcpp.png", "/usr/share/pixmaps/linuxdcpp.png")

    pisitools.dodoc("Changelog.txt", "Credits.txt", "License.txt", "Readme.txt")
