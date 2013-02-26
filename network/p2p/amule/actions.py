#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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
