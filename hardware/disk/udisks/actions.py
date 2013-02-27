#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-gtk-doc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #shelltools.chmod("%s/etc/profile.d/*.sh" % get.installDIR(), mode=0644)

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
