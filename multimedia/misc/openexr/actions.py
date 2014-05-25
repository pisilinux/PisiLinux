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
    pisitools.flags.add("-pthread -I/usr/include/OpenEXR -I/usr/include/libdrm")
    pisitools.ldflags.add("-lImath -lHalf -lIex -lIexMath -lIlmThread -lpthread")
    shelltools.system("./bootstrap")
    autotools.configure("--enable-shared \
                         --disable-static")

def build():
    autotools.make()

def install():
    # documents and examples go to "/usr/share/OpenEXR" without these parameters
    docdir = "/usr/share/doc/%s" % get.srcNAME()
    examplesdir = "%s/examples" % docdir
    autotools.rawInstall("DESTDIR=%s docdir=%s examplesdir=%s" % (get.installDIR(), docdir, examplesdir))

    pisitools.dodoc("AUTHORS", "ChangeLog","NEWS", "README","LICENSE")
