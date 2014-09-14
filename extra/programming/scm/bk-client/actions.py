#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="."

def setup():
    shelltools.system("sh bk-client2.0.shar")

    # Change function name, getline conflicts with 4.5.x
    shelltools.system("patch -Np0 -i %s/gcc-4.5-getline.patch" % get.workDIR())

def build():
    shelltools.cd("bk-client2.0")
    autotools.make()

def install():
    shelltools.cd("bk-client2.0")
    pisitools.insinto("/usr/bin","bkf","bk-client")
