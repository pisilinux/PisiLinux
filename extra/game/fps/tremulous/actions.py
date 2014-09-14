#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

import os

WorkDir = "tremulous-1.2.beta1"
datadir = "/usr/share/tremulous"

arch = "x86_64" if get.ARCH() == "x86_64" else "x86"
builddir = "build/release-linux-%s" % arch
archparam = "ARCH=x86_64" if get.ARCH() == "x86_64" else ""

def setup():
    for i in ["SDL12", "AL", "libcurl", "libspeex", "libs"]:
        if shelltools.isDirectory("src/%s" % i):
            shelltools.unlinkDir("src/%s" % i)

    pisitools.dosed("misc/server.cfg", "set sv_hostname.*", 'set sv_hostname "Tremulous Server on PisiLinux"')

def build():
    autotools.make('BUILD_CLIENT=1 \
                    BUILD_CLIENT_SMP=1 \
                    BUILD_SERVER=1 \
                    BUILD_GAME_SO=0 \
                    BUILD_GAME_QVM=0 \
                    CC=%s \
                    DEFAULT_BASEDIR=%s \
                    USE_CODEC_VORBIS=1 \
                    USE_OPENAL=1 \
                    USE_LOCAL_HEADERS=0 \
                    USE_INTERNAL_SPEEX=0 \
                    USE_INTERNAL_ZLIB=0 \
                    GENERATE_DEPENDENCIES=0 \
                    %s \
                    OPTIMIZE="%s -fno-strict-aliasing -ffast-math"' % (get.CC(), datadir, archparam, get.CFLAGS()))

def install():
    pisitools.insinto("/usr/share/pixmaps", "misc/tremulous.xpm")
    pisitools.dodir("%s/base" % datadir)

    shelltools.move("%s/tremulous.%s" % (builddir, arch), "%s/tremulous" % builddir)
    shelltools.move("%s/tremulous-smp.%s" % (builddir, arch), "%s/tremulous-smp" % builddir)
    shelltools.move("%s/tremded.%s" % (builddir, arch), "%s/tremulous-server" % builddir)

    for f in ["tremulous", "tremulous-smp", "tremulous-server"]:
        shelltools.chmod("%s/%s" % (builddir, f), 0755)
        pisitools.dobin("%s/%s" % (builddir, f))

    for f in shelltools.ls("%s/base/" % builddir):
        if f.endswith(".so") and shelltools.isFile("%s/base/%s" % (builddir, f)):
            shelltools.chmod("%s/base/%s" % (builddir, f), 0755)
            pisitools.dobin("%s/base/%s" % (builddir, f), "%s/base/" % datadir)


