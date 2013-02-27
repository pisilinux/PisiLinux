#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i -e 's/png_ptr->jmpbuf/png_jmpbuf(png_ptr)/' src/xsane-save.c")
    shelltools.system("sed -i -e 's/netscape/xdg-open/' src/xsane.h")
    shelltools.unlink("include/config.h")

    shelltools.makedirs("withgimp")
    shelltools.makedirs("withoutgimp")

    shelltools.cd("withgimp")
    shelltools.sym("../configure", "configure")

    autotools.configure("--enable-gimp")

    shelltools.cd("../withoutgimp")
    shelltools.sym("../configure", "configure")
    autotools.configure("--disable-gimp")

def build():
    autotools.make("-C withgimp")
    autotools.make("-C withoutgimp")

def install():
    autotools.rawInstall("-C withoutgimp DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/lib/gimp/2.0/plug-ins", "withgimp/src/xsane")

    pisitools.dodoc("xsane.*")
    pisitools.remove("/usr/share/doc/xsane/xsane.spe*")
    pisitools.remove("/usr/share/doc/xsane/xsane.RPM")

    pisitools.removeDir("/usr/sbin")
