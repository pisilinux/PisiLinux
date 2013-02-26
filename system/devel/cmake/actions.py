# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    # Fix sandbox violation
    #shelltools.export("BZR_HOME", get.workDIR())

    autotools.rawConfigure("--parallel=%s \
                            --system-libs \
                            --no-qt-gui \
                            --prefix=/usr \
                            --datadir=/share/cmake \
                            --docdir=/share/doc/cmake \
                            --mandir=/share/man" % get.makeJOBS().replace("-j", ""))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
