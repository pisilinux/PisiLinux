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
