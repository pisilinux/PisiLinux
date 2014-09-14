#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

ARCH = get.ARCH().replace("686", "386")

builddir = "build/release-linux-%s" % ARCH
datadir = "/usr/share/WoP"
NoStrip = ["%s/wop" % datadir]

def setup():
    shelltools.system("rm -rf code/libcurl")
    shelltools.system("rm -rf code/SDL12")
    shelltools.system("rm -rf code/zlib")
    shelltools.system("rm -rf code/libspeex")
    shelltools.system("rm -rf code/libtheora")
    shelltools.system("rm -rf code/libvorbis")
    shelltools.system("rm -rf code/libogg")
    shelltools.system("rm -rf code/jpeg-8c")

    pisitools.dosed("Makefile", "-O3", "%s -DUSE_ACTOR_DEFAULTS" % get.CFLAGS())
    pisitools.dosed("Makefile", "CC=gcc", "CC=%s" % get.CC())

def build():
    autotools.make("DEFAULT_BASEDIR=%s \
                    BUILD_CLIENT=1 \
                    BUILD_SERVER=1 \
                    BUILD_CLIENT_SMP=1 \
                    BUILD_GAME_SO=1 \
                    BUILD_GAME_QVM=1 \
                    USE_CODEC_VORBIS=1 \
                    USE_INTERNAL_SPEEX=0 \
                    USE_INTERNAL_ZLIB=0 \
                    USE_INTERNAL_JPEG=0 \
                    USE_INTERNAL_DLOPEN=0 \
                    USE_LOCAL_HEADERS=0 \
                    DEBUG_BUILD=NO" % (datadir))

def install():
    for i in ["wop", "wopded"]:
        pisitools.dobin("build/release-linux-%s/%s.%s" % (ARCH, i, ARCH))

    pisitools.rename("/usr/bin/wop.%s" % ARCH, "WoP")
    pisitools.rename("/usr/bin/wopded.%s" % ARCH, "WoP-server")

    pisitools.doexe("%s/baseq3/*.so" % builddir, "%s/baseq3" % datadir)
    pisitools.insinto("%s/baseq3/vm/" % datadir, "%s/baseq3/vm/*" % builddir)

    pisitools.doexe("%s/*.so" % builddir, "%s" % datadir)

    pisitools.insinto("%s/missionpack" % datadir, "%s/missionpack" % builddir)

    pisitools.dodoc("*.txt", "*-README")
