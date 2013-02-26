#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file `http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import scons
from pisi.actionsapi import get

def setup():
    # Set python version in user-config
    #pisitools.dosed("user-config.py", "@LIB@", "/usr/lib")
    #pisitools.dosed("user-config.py", "@PYVER@", get.curPYTHON().replace("python", ""))
    #pisitools.dosed("user-config.py", "@CC@", get.CC())
    #pisitools.dosed("user-config.py", "@CXX@", get.CXX())
    #pisitools.dosed("user-config.py", "^WITH_BF_FFMPEG = 'false'.*", "WITH_BF_FFMPEG = 'true'")

    # Drop bundled libraries
    for d in ["ffmpeg", "x264", "xvidcore", "fftw", "glew", "libopenjpeg", "ode", "qhull"]:
        shelltools.system("rm -rf extern/%s" % d)
    shelltools.system("rm -rf scons")

def build():
    #scons.make("WITH_BF_PLAYER=1 WITH_BF_OPENAL=1 BF_FANCY=0")
    shelltools.export("RPM_OPT_FLAGS", get.CFLAGS())
    scons.make("WITH_BF_PLAYER=1 WITH_BF_OPENAL=1 WITH_BF_INTERNATIONAL=1 BF_QUIET=0 BF_NUMJOBS=%s" % get.makeJOBS().replace("-j", "1"))

    shelltools.makedirs("release/plugins/include")
    shelltools.copy("source/blender/blenpluginapi/*.h", "release/plugins/include")

    shelltools.chmod("release/plugins/bmake", 0755)
    autotools.make("-C release/plugins")

def install():
    pisitools.insinto("/usr/bin","install/linux2/blender","blender-bin")
    pisitools.dobin("install/linux2/blenderplayer")

    # Install plugins
    for d in ("/usr/lib/blender/scripts", "/usr/lib/blender/plugins/sequence", "/usr/lib/blender/plugins/texture"):
        pisitools.dodir(d)
    pisitools.insinto("/usr/lib/blender/plugins/texture","release/plugins/texture/*.so")
    pisitools.insinto("/usr/lib/blender/plugins/sequence","release/plugins/sequence/*.so")

    # Install miscellaneous files
    pisitools.insinto("/usr/share/blender", "release/scripts")

    pisitools.insinto("/usr/share", "install/linux2/.blender/locale")
    pisitools.insinto("/usr/share/blender", "install/linux2/.blender/.Blanguages")
    pisitools.insinto("/usr/share/blender", "install/linux2/.blender/.bfont.ttf")
    pisitools.insinto("/usr/share/blender", "release/VERSION")

    # chmod 644 for scripts
    shelltools.chmod("%s/usr/share/blender/scripts/*.py" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/blender/scripts/bpymodules/blend2renderinfo.py" % get.installDIR(), 0755)

    # Headers
    pisitools.insinto("/usr/include/blender", "install/linux2/plugins/include/*.h")

    #Install desktop file
    pisitools.insinto("/usr/share/applications", "release/freedesktop/blender.desktop")

    #Install icon files
    import os.path
    for size in map(lambda x: os.path.basename(x), shelltools.ls("release/freedesktop/icons/")):
        pisitools.dodir("/usr/share/icons/hicolor/%s/apps" % size)
        if size == "scalable":
            pisitools.insinto("/usr/share/icons/hicolor/%s/apps" % size, "release/freedesktop/icons/%s/*.svg" % size)
        else:
            pisitools.insinto("/usr/share/icons/hicolor/%s/apps" % size, "release/freedesktop/icons/%s/*.png" % size)

    pisitools.dodoc("COPYING", "README")
