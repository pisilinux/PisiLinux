#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/plugins/Input/cdaudio/decoder_cdaudio.cpp", "cdio\/cdda\.h", r"cdio/paranoia/cdda.h")
    cmaketools.configure("-DUSE_PULSE=TRUE \
                          -DUSE_ALSA=TRUE \
                          -DUSE_FFMPEG=TRUE \
                          -DUSE_FFMPEG_LEGACY=OFF \
                          -DUSE_CDA=TRUE \
                          -DUSE_VORBIS=TRUE \
                          -DUSE_AAC=TRUE \
                          -DUSE_LADSPA=TRUE \
                          -DUSE_COVER=TRUE \
                          -DUSE_KDENOTIFY=TRUE \
                          -DUSE_ENCA=TRUE \
                          -DUSE_MPLAYER=TRUE \
                          -DUSE_FLAC=TRUE \
                          -DUSE_MPRIS=TRUE \
                          -DUSE_HAL=OFF \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DCMAKE_SKIP_INSTALL_RPATH=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog*", "README*")
