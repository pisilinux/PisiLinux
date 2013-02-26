#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    shelltools.system("jam")

def install():
    shelltools.system('jam -sDESTDIR="%s" \
                       -sappdocdir="/%s/%s" \
                       -sapplicationsdir="/usr/share/applications" \
                       -spixmapsdir="/usr/share/pixmaps" \
                       install' % (get.installDIR(), get.docDIR(), get.srcNAME()))

    # We will use our own desktop file
    pisitools.remove("/usr/share/applications/lincity-ng.desktop")
