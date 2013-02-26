#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("WXRC", "/usr/bin/wxrc-2.8")
    shelltools.export("LDFLAGS", "%s -lpthread" % get.LDFLAGS())
    autotools.configure("--disable-static \
                         --with-wx-config=/usr/bin/wx-config \
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
