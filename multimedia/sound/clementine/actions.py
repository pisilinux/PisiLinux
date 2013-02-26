#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("dist/clementine.desktop", "Icon=application-x-clementine", "Icon=clementine")
    for i in ["libprojectm", "qxt", "qtiocompressor", "libechonest"]:
        shelltools.unlinkDir("3rdparty/%s" % (i))

    # QTSINGLEAPPLICATION is builtin since we need to patch Qt just for this package and Gökçen has given OK
    # for using built-in qtsingleapplication.
    cmaketools.configure("-DUSE_SYSTEM_QXT=ON \
                          -Werror=OFF \
                          -DENABLE_LIBLASTFM=ON \
                          -DUSE_SYSTEM_QTSINGLEAPPLICATION=OFF \
                          -DENABLE_SPOTIFY=OFF\
                          -DENABLE_SPOTIFY_BLOB=OFF\
                          -DUSE_SYSTEM_GMOCK=ON \
                          -DSTATIC_SQLITE=OFF \
                          -DUSE_SYSTEM_PROJECTM=ON \
                          -DENABLE_WIIMOTEDEV=ON \
                          -DENABLE_LIBGPOD=ON \
                          -DENABLE_IMOBILEDEVICE=ON \
                          -DENABLE_LIBMTP=ON \
                          -DENABLE_GIO=ON \
                          -DENABLE_VISUALISATIONS=ON \
                          -DENABLE_SCRIPTING_PYTHON=ON \
                          -DENABLE_SCRIPTING_ARCHIVES=ON \
                          -DENABLE_REMOTE=OFF \
                          -DBUNDLE_PROJECTM_PRESETS=OFF", sourceDir=".")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    for i in ("16","32","64"):
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (i,i), "dist/clementine_%s.png" % i, "clementine.png")

    pisitools.insinto("/usr/share/clementine/locale", "src/translations/*.qm")
    pisitools.dosym("/usr/share/icons/hicolor/64x64/apps/clementine.png", "/usr/share/pixmaps/clementine.png")

    pisitools.dodoc("Changelog", "COPYING")
