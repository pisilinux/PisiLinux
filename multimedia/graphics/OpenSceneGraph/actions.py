#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DLIB_POSTFIX=''")

def build():
    cmaketools.make("-j1")

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/lib/pkgconfig", "packaging/pkgconfig/*.pc")

    pisitools.dodoc("AUTHORS.txt", "ChangeLog", "LICENSE.txt", "NEWS.txt", "README.txt")
