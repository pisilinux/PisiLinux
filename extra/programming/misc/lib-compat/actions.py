#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools

def install():
    # install /lib/ld-linux.so.1.9.11
    pisitools.dolib_so("ld-linux.so.1*", "/lib")
    shelltools.unlink("ld-linux.so.1*")

    pisitools.remove("/lib/ld-linux.so.1")
    pisitools.dosym("ld-linux.so.1.9.11", "/lib/ld-linux.so.1")

    # install other compatibilty libraries
    pisitools.dolib_so("*.so*")
    libtools.preplib()
