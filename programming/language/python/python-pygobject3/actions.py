#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure", "-Werror=format", "#-Werror=format")
    shelltools.makedirs("build-python2")
    shelltools.makedirs("build-python3")

    shelltools.cd("build-python3")
    shelltools.export("PYTHON", "/usr/bin/python3.3")
    shelltools.system("../configure --prefix=/usr \
                       --localstatedir=/var \
                       --disable-static")

    shelltools.cd("../build-python2")
    shelltools.export("PYTHON", "/usr/bin/python2.7")
    shelltools.system("../configure --prefix=/usr \
                       --localstatedir=/var \
                       --disable-static")

def build():
    shelltools.cd("build-python3")
    autotools.make()

    shelltools.cd("../build-python2")
    autotools.make()

def install():
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")

    shelltools.cd("build-python3")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../build-python2")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())