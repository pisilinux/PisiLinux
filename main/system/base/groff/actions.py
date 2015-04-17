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
    #autotools.autoreconf("-fi")
    shelltools.export("PAGE", "a4")
    autotools.configure("--prefix=/usr \
                         --without-x")

def build():
    #shelltools.export("LC_ALL", "C")
    autotools.make()

def install():
    pisitools.dodir("/usr")
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # required by man
    pisitools.dosym("eqn", "/usr/bin/geqn")
    pisitools.dosym("tbl", "/usr/bin/gtbl")
    pisitools.dosym("soelim", "usr/bin/zsoelim")
    pisitools.dodoc("ChangeLog", "NEWS", "PROBLEMS", "PROJECTS", "README")
