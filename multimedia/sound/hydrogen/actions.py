#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

#WorkDir = "hydrogen-%s" % get.srcVERSION().replace("_", "-")

def build():
    shelltools.export("QTDIR", get.qtDIR())
    scons.make("prefix=/usr \
                DESTDIR=%s \
                lash=1 \
                portaudio=1 \
                portmidi=1 \
                oss=0 \
                optflags=\"%s\"" % (get.installDIR(), get.CFLAGS()))

def install():
    shelltools.export("QTDIR", get.qtDIR())
    scons.install(prefix="/usr")

    pisitools.domove("/usr/share/pixmaps/h2-icon.svg", "/usr/share/icons/hicolor/scalable/apps")
    pisitools.removeDir("/usr/share/pixmaps")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README.txt", "COPYING")
