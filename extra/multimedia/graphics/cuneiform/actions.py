#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools


def setup():
    replace = (r'(set[(]CMAKE_SHARED_LINKER_FLAGS "[^"]*)', r'\1 %s' \
            % get.LDFLAGS())
    pisitools.dosed("cuneiform_src/CMakeLists.txt", *replace)
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release", sourceDir="..")


def build():
    shelltools.cd("build")
    cmaketools.make()


def install():
    shelltools.cd("build")
    cmaketools.install()

    pisitools.dodoc("../issues.txt", "../readme.txt")
