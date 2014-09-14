#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4
from pisi.actionsapi import get

def setup():
	pisitools.dosed("src/mumble/AudioInput.cpp", "CELT_SET_VBR_RATE", "CELT_SET_BITRATE")
	for i in ["speex", "speexbuild", "celt-0.11.0-build", "celt-0.11.0-src"]:
		shelltools.unlinkDir(i)
	qt4.configure(parameters='QMAKE_CFLAGS_RELEASE="%s" \
                  QMAKE_CXXFLAGS_RELEASE="%s" \
                  CONFIG+=no-bundled-speex \
                  CONFIG+=no-bundled-celt \
                  CONFIG+=no-update \
                  CONFIG+=no-ice \
                  CONFIG+=no-g15 \
                  CONFIG+=no-embed-qt-translations \
                  DEFINES+=PLUGIN_PATH=/usr/lib/mumble \
                  DEFINIES+=NO_UPDATE_CHECK \
                  DEFINES+=DEFAULT_SOUNDSYSTEM=PulseAudio' % (get.CFLAGS(), get.CXXFLAGS()))
	
def build():
    qt4.make()

def install():
    pisitools.dobin("release/mumble")
    pisitools.dobin("scripts/mumble-overlay")
    pisitools.dosbin("release/murmurd")

    pisitools.insinto("/usr/lib/mumble", "release/*.so*")
    pisitools.doexe("release/plugins/*.so", "/usr/lib/mumble")

    pisitools.insinto("/usr/share/applications", "scripts/mumble.desktop")
    pisitools.insinto("/usr/share/kde4/services", "scripts/mumble.protocol")
    pisitools.insinto("/usr/share/mumble/translations", "src/mumble/*.qm")

    for size in ("16x16", "32x32", "48x48", "64x64"):
        pisitools.insinto("/usr/share/icons/hicolor/scalable/apps", "icons/mumble.svg")

    pisitools.insinto("/etc/murmur", "scripts/murmur.ini")
    pisitools.dosym("murmur/murmur.ini", "/etc/mumble-server.ini")

    pisitools.dodir("/var/lib/mumble-server")
    pisitools.dodir("/var/log/mumble-server")
    pisitools.dodir("/run/mumble-server")

    pisitools.doman("man/*")
    pisitools.dodoc("CHANGES", "LICENSE", "README*", "scripts/weblist*")
