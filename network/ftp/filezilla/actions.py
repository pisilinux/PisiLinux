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
    shelltools.export("WXRC", "/usr/bin/wxrc")
    shelltools.export("LDFLAGS", "%s -lpthread" % get.LDFLAGS())
    pisitools.dosed("data/filezilla.desktop", "Icon=filezilla", "Icon=/usr/share/pixmaps/filezilla.png")
    autotools.configure("--disable-static \
                         --with-wx-config=/usr/bin/wxconfig \
                         --disable-manualupdatecheck \
                         --disable-autoupdatecheck \
                         --with-tinyxml=builtin")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # move fzdefaults.xml.example to /usr/share/filezilla
    pisitools.domove("/usr/share/filezilla/docs/fzdefaults.xml.example", "/usr/share/filezilla")
    pisitools.removeDir("/usr/share/filezilla/docs")

    pisitools.dodoc("ChangeLog", "README", "AUTHORS")