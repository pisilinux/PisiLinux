#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("CXXFLAGS", "%s -D__STDC_CONSTANT_MACROS" % get.CXXFLAGS())

def setup():
    cmaketools.configure('-DLIB_POSTFIX="" \
                          -DCMAKE_RELWITHDEBINFO_POSTFIX=""')

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS.txt", "ChangeLog", "LICENSE.txt", "NEWS.txt", "README.txt")
