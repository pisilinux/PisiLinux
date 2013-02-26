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
    autotools.configure("--with-default-dict=/usr/share/cracklib/pw_dict \
                         --disable-static")

def build():
    autotools.make("all")

def install():
    autotools.install()

    # Create dictionary files
    shelltools.system("cat /usr/share/cracklib/cracklib-small|%s/usr/sbin/cracklib-packer %s/usr/share/cracklib/pw_dict" % (get.installDIR(),get.installDIR()))

    # pisitools.domo("po/tr.po","tr","cracklib.mo")
    pisitools.dodoc("ChangeLog", "README*", "NEWS", "COPYING.LIB", "AUTHORS")
