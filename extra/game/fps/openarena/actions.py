#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

# 0.8.5 is a patch over 0.8.1
WorkDir = "openarena-engine-source-0.8.8"
#WorkDir = "openarena-engine-%s" % get.srcVERSION()

build_arch = "x86_64" if get.ARCH() == "x86_64" else "i386"

builddir = "build/release-linux-%s" % build_arch
datadir = "/usr/share/openarena"

def build():
    autotools.make('DEFAULT_BASEDIR=/usr/share/openarena BUILD_SERVER=1 BUILD_CLIENT=1 BUILD_CLIENT_SMP=1')
#OPTIMIZE="%s" \
#DEFAULT_BASEDIR="%s" \
#BUILD_STANDALONE=1 \
#BUILD_SERVER=1 \
#BUILD_CLIENT=1 \
#BUILD_CLIENT_SMP=1 \
#USE_SDL=1 \
#USE_OPENAL=1 \
#USE_CURL=1 \
#USE_CODEC_VORBIS=1 \
#USE_LOCAL_HEADERS=1' % (get.CFLAGS(), datadir))

def install():
    pisitools.insinto("/usr/bin", "%s/oa_ded.%s" % (builddir, build_arch), "openarena-server")
    pisitools.insinto("/usr/bin", "%s/openarena.%s" % (builddir, build_arch), "openarena")
    pisitools.insinto("/usr/bin", "%s/openarena-smp.%s" % (builddir, build_arch), "openarena-smp")
    #pisitools.dodoc("BUGS", "ChangeLog", "NOTTODO", "TODO", "README", "*.txt") 
