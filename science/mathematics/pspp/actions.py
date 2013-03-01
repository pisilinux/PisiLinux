#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-libplot \
                         --with-libncurses \
                         --enable-nls \
                         --disable-static \
                         --disable-rpath \
                         --with-x \
                         --with-gui")

def build():
    autotools.make()
    autotools.make("html")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/icons/hicolor/16x16/apps", "src/ui/gui/psppicon.png", "psppire.png")
    pisitools.insinto("/usr/share/icons/hicolor/64x64/apps", "src/ui/gui/pspplogo.png", "psppire.png")

    for f in ["ABOUT-NLS", "AUTHORS", "ChangeLog", "NEWS", "ONEWS", "README", "THANKS", "TODO"]:
        pisitools.dodoc(f)

    pisitools.insinto("%s/%s/examples" % (get.docDIR(), get.srcNAME()), "examples/descript.stat")

    pisitools.dohtml("doc/pspp.html/*.html")

