#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    # llvm 3.4 compatibility
    shelltools.system("sed -i '/JITExceptionHandling/d' src/scripting/abc.cpp")
    cmaketools.configure('-DCMAKE_BUILD_TYPE=release \
                          -DCOMPILE_PLUGIN=1 \
                          -DPLUGIN_DIRECTORY="/usr/lib/browser-plugins/" \
                          -DENABLE_SOUND=1 \
                          -DGNASH_EXE_PATH=/usr/bin/gtk-gnash', installPrefix="/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CONTRIBUTORS", "ChangeLog", "COPYING.*", "README")