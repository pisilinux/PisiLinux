#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import qt4
from pisi.actionsapi import get

import os

WorkDir = "qtbase-opensource-src-5.0.0-beta2"

qtbase = qt4.prefix
# absoluteWorkDir = "%s/%s" % (get.workDIR(), WorkDir)

def setup():
    #make sure we don't use them
    for d in ('libjpeg', 'freetype', 'libpng', 'zlib'):
        shelltools.unlinkDir("src/3rdparty/%s" % d)

    """filteredCFLAGS = get.CFLAGS().replace("-g3", "-g")
    filteredCXXFLAGS = get.CXXFLAGS().replace("-g3", "-g")

    vars = {"PARDUS_CC" :       get.CC(),
            "PARDUS_CXX":       get.CXX(),
            "PARDUS_CFLAGS":    filteredCFLAGS,
            "PARDUS_LDFLAGS":   get.LDFLAGS()}

    for k, v in vars.items():
        pisitools.dosed("mkspecs/common/g++-base.conf", k, v)
        pisitools.dosed("mkspecs/common/g++-unix.conf", k, v)

    shelltools.export("CFLAGS", filteredCFLAGS)
    shelltools.export("CXXFLAGS", filteredCXXFLAGS)"""

    #-no-pch makes build ccache-friendly
    autotools.rawConfigure("-pch \
                            -v \
                            -fast \
                            -glib \
                            -no-sql-sqlite2 \
                            -system-sqlite \
                            -system-zlib \
                            -system-libpng \
                            -system-libjpeg \
                            -plugin-sql-sqlite \
                            -plugin-sql-odbc \
                            -plugin-sql-mysql \
                            -plugin-sql-psql \
                            -plugin-sql-ibase \
                            -I/usr/include/mysql/ \
                            -I/usr/include/firebird/ \
                            -I/usr/include/postgresql/server/ \
                            -release \
                            -icu \
                            -no-separate-debug-info \
                            -no-rpath \
                            -openssl-linked \
                            -dbus-linked \
                            -opensource \
                            -reduce-relocations \
                            -prefix %s \
                            -libdir %s \
                            -docdir /usr/share/doc/qt \
                            -examplesdir /usr/lib/qt/examples \
                            -plugindir /usr/lib/qt/plugins \
                            -translationdir /usr/share/qt/translations \
                            -sysconfdir %s \
                            -datadir /usr/share/qt \
                            -importdir /usr/lib/qt/imports \
                            -headerdir %s \
                            -confirm-license " % (qt4.prefix, qt4.libdir, qt4.sysconfdir, qt4.includedir))

def build():
    autotools.make()

def install():
    qt4.install()
    pisitools.dodir(qt4.bindir)

    #Remove phonon, we use KDE's phonon but we have to build Qt with Phonon support for webkit and some other stuff
    #pisitools.remove("%s/libphonon*" % qt4.libdir)
    #pisitools.removeDir("%s/phonon" % qt4.includedir)
    # -no-phonon-backend : pisitools.removeDir("%s/phonon_backend" % qt4.plugindir)
    #pisitools.remove("%s/pkgconfig/phonon*" % qt4.libdir)
    # Phonon 4.5 provides libphononwidgets.so file
    #pisitools.remove("%s/designer/libphononwidgets.so" % qt4.plugindir)

    # Turkish translations
    shelltools.export("LD_LIBRARY_PATH", "%s%s" % (get.installDIR(), qt4.libdir))
    #shelltools.system("%s%s/lrelease l10n-tr/*.ts" % (get.installDIR(), qt4.bindir))
    #pisitools.insinto(qt4.translationdir, "l10n-tr/*.qm")

    # Fix all occurances of WorkDir in pc files
    #pisitools.dosed("%s%s/pkgconfig/*.pc" % (get.installDIR(), qt4.libdir), "%s/qt-x11-opensource-src-%s" % (get.workDIR(), get.srcVERSION()), qt4.prefix)

    mkspecPath = "/usr/share/qt/mkspecs"

    for root, dirs, files in os.walk("%s/usr" % get.installDIR()):
        # Remove unnecessary spec files..
        if root.endswith(mkspecPath):
            for dir in dirs:
                if not dir.startswith("linux") and dir not in ["common","qws","features","default"]:
                    pisitools.removeDir(os.path.join(mkspecPath,dir))
        for name in files:
            if name.endswith(".prl"):
                pisitools.dosed(os.path.join(root, name), "^QMAKE_PRL_BUILD_DIR.*", "")

    pisitools.dodoc("LGPL_EXCEPTION.txt", "LICENSE.*")
