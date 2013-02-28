#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    #amulegui is buggy: http://wiki.amule.org/index.php/AMuleGUI
    autotools.configure("--enable-amulecmd \
                         --enable-webserver \
                         --enable-amule-daemon \
                         --enable-optimize \
                         --enable-ccache \
                         --enable-alc \
                         --enable-cas \
                         --enable-wxcas \
                         --disable-amule-gui \
                         --enable-alcc \
                         --enable-geoip \
                         --disable-rpath \
                         --disable-debug")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
