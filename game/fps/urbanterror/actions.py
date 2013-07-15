#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#
# For ioquake sources svn://svn.icculus.org/quake3/trunk
# For bunch of updates http://www.www0.org/urt/
#
# Tarball is created with ioquake revision 1807, copying files of
# http://www.www0.org/urt/ioq3-1807-urt-251210-git.tar.lzma
# and applying ioq3-1807-urt-251210-git.patch in ioq3
#

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", "-"))
arch = get.ARCH().replace("i686", "i386")

builddir = "build/release-linux-%s" % arch
datadir = "/usr/share/urbanterror"

cflags = "%s -I/usr/include/freetype2" % get.CFLAGS()

def setup():
    for i in ["code/SDL12", "code/libs/win32"]:
        if shelltools.isDirectory(i):
            shelltools.unlinkDir(i)

def build():
    autotools.make('CC="%s" \
                    ARCH="%s" \
                    OPTIMIZE="%s" \
                    DEFAULT_BASEDIR="%s" \
                    BUILD_SERVER=1 \
                    BUILD_CLIENT=1 \
                    BUILD_CLIENT_SMP=1 \
                    BUILD_GAME_SO=1 \
                    USE_SDL=1 \
                    USE_OPENAL=1 \
                    USE_FREETYPE=0 \
                    USE_CURL=1 \
                    USE_CODEC_VORBIS=1 \
                    USE_VOIP=1 \
                    USE_INTERNAL_SPEEX=0 \
                    USE_INTERNAL_ZLIB=0 \
                    USE_LOCAL_HEADERS=0 \
                    release' % (get.CC(), arch, cflags, datadir))
                    #BUILD_GAME_QVM=0 \


def install():
    pisitools.dobin("%s/ioquake3.%s" % (builddir, arch))
    pisitools.dobin("%s/ioquake3-smp.%s" % (builddir, arch))
    pisitools.dobin("%s/ioq3ded.%s" % (builddir, arch))

    pisitools.rename("/usr/bin/ioquake3.%s" % arch, "urbanterror")
    pisitools.rename("/usr/bin/ioquake3-smp.%s" % arch, "urbanterror-smp")
    pisitools.rename("/usr/bin/ioq3ded.%s" % arch, "urbanterror-server")

    pisitools.doexe("%s/baseq3/*.so" % builddir, "%s/baseq3" % datadir)
    #pisitools.doexe("%s/missionpack/*.so" % builddir, "%s/missionpack" % datadir)

    pisitools.insinto("%s/baseut4/" % datadir, "q3ut4/*")

    pisitools.dodoc("BUGS", "ChangeLog", "*.txt", "NOTTODO", "README", "TODO")

