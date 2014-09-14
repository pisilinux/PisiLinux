#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import qt4
from pisi.actionsapi import get

import os

WorkDir = "qt-everywhere-opensource-src-%s" % get.srcVERSION().replace('_','-').replace('pre1', 'tp')

qtbase = qt4.prefix
absoluteWorkDir = "%s/%s" % (get.workDIR(), WorkDir)

def setup():
    pisitools.flags.add("-I/usr/include/gtk-2.0/gdk")
    #make sure we don't use them
    for d in ('libjpeg', 'freetype', 'libpng', 'zlib', 'libtiff'):
        shelltools.unlinkDir("src/3rdparty/%s" % d)

    filteredCFLAGS = get.CFLAGS().replace("-g3", "-g")
    filteredCXXFLAGS = get.CXXFLAGS().replace("-g3", "-g")

    vars = {"PISILINUX_CC" :       get.CC() + (" -m32" if get.buildTYPE() == "emul32" else ""),
            "PISILINUX_CXX":       get.CXX() + (" -m32" if get.buildTYPE() == "emul32" else ""),
            "PISILINUX_CFLAGS":    filteredCFLAGS + (" -m32" if get.buildTYPE() == "emul32" else ""),
            "PISILINUX_LDFLAGS":   get.LDFLAGS() + (" -m32" if get.buildTYPE() == "emul32" else "")}

    for k, v in vars.items():
        pisitools.dosed("mkspecs/common/g++-base.conf", k, v)
        pisitools.dosed("mkspecs/common/g++-unix.conf", k, v)

    shelltools.export("CFLAGS", filteredCFLAGS)
    shelltools.export("CXXFLAGS", filteredCXXFLAGS)
    #check that dosed commands without releated patches
    pisitools.dosed("mkspecs/common/gcc-base-unix.conf", "\-Wl,\-rpath,")
    pisitools.dosed("mkspecs/common/gcc-base.conf", "\-O2", filteredCFLAGS)
    pisitools.dosed("mkspecs/common/gcc-base.conf", "^(QMAKE_LFLAGS\s+\+=)", r"\1 %s" % get.LDFLAGS())

    if not get.buildTYPE() == "emul32":
        #-no-pch makes build ccache-friendly
        options = "-no-pch \
                   -v \
                   -stl \
                   -fast \
                   -qdbus \
                   -qvfb \
                   -glib \
                   -no-sql-sqlite2 \
                   -system-sqlite \
                   -system-zlib \
                   -system-libpng \
                   -system-libjpeg \
                   -system-libtiff \
                   -system-libmng \
                   -plugin-sql-sqlite \
                   -plugin-sql-odbc \
                   -plugin-sql-psql \
                   -plugin-sql-ibase \
                   -I/usr/include/firebird/ \
                   -I/usr/include/postgresql/server/ \
                   -release \
                   -no-separate-debug-info \
                   -phonon \
                   -no-phonon-backend \
                   -webkit \
                   -no-rpath \
                   -openssl-linked \
                   -dbus-linked \
                   -xmlpatterns \
                   -opensource \
                   -reduce-relocations \
                   -prefix %s \
                   -libdir %s \
                   -docdir %s \
                   -examplesdir %s \
                   -demosdir %s\
                   -plugindir %s \
                   -translationdir %s \
                   -sysconfdir %s \
                   -datadir %s \
                   -importdir %s \
                   -headerdir %s \
                   -confirm-license " % (qt4.prefix, qt4.libdir, qt4.docdir, qt4.examplesdir, qt4.demosdir, qt4.plugindir, qt4.translationdir, qt4.sysconfdir, qt4.datadir, qt4.importdir, qt4.includedir)
    else:
        pisitools.dosed("mkspecs/linux-g++-64/qmake.conf", "-m64", "-m32")
        shelltools.export("LDFLAGS", "-m32 %s" % get.LDFLAGS())
        options = "-no-pch \
                   -v \
                   -prefix /usr \
                   -libdir /usr/lib32 \
                   -plugindir /usr/lib32/qt/plugins \
                   -importdir /usr/lib32/qt/imports \
                   -datadir /usr/share/qt \
                   -translationdir /usr/share/qt/translations \
                   -sysconfdir /etc \
                   -system-sqlite \
                   -no-phonon \
                   -no-phonon-backend \
                   -webkit \
                   -graphicssystem raster \
                   -openssl-linked \
                   -nomake demos \
                   -nomake examples \
                   -nomake docs \
                   -nomake tools \
                   -optimized-qmake \
                   -no-rpath \
                   -dbus-linked \
                   -reduce-relocations \
                   -no-openvg \
                   -confirm-license \
                   -opensource "

    autotools.rawConfigure(options)

def build():
    shelltools.export("LD_LIBRARY_PATH", "%s/lib:%s" % (get.curDIR(), get.ENV("LD_LIBRARY_PATH")))
    autotools.make()

def install():
    if get.buildTYPE() == "emul32":
        qt4.install("INSTALL_ROOT=%s32" % get.installDIR())
        shelltools.move("%s32/usr/lib32" % get.installDIR(), "%s/usr" % get.installDIR())
        return

    qt4.install()
    pisitools.dodir(qt4.bindir)

    #Remove phonon, we use KDE's phonon but we have to build Qt with Phonon support for webkit and some other stuff
    pisitools.remove("%s/libphonon*" % qt4.libdir)
    pisitools.removeDir("%s/phonon" % qt4.includedir)
    if shelltools.isDirectory("%s/%s/phonon_backend" % (get.installDIR(), qt4.plugindir)):
        pisitools.removeDir("%s/phonon_backend" % qt4.plugindir)
    pisitools.remove("%s/pkgconfig/phonon*" % qt4.libdir)
    # Phonon 4.5 provides libphononwidgets.so file
    pisitools.remove("%s/designer/libphononwidgets.so" % qt4.plugindir)

    #Remove lost /usr/tests directory
    pisitools.removeDir("usr/tests")

    # Turkish translations
    shelltools.export("LD_LIBRARY_PATH", "%s%s" % (get.installDIR(), qt4.libdir))
    shelltools.system("%s%s/lrelease l10n-tr/*.ts" % (get.installDIR(), qt4.bindir))
    pisitools.insinto(qt4.translationdir, "l10n-tr/*.qm")

    # Fix all occurances of WorkDir in pc files
    pisitools.dosed("%s%s/pkgconfig/*.pc" % (get.installDIR(), qt4.libdir), "%s/qt-x11-opensource-src-%s" % (get.workDIR(), get.srcVERSION()), qt4.prefix)

    mkspecPath = "%s/mkspecs" % qtbase

    for root, dirs, files in os.walk("%s%s" % (get.installDIR(), qtbase)):
        # Remove unnecessary spec files..
        if root.endswith(mkspecPath):
            for dir in dirs:
                if not dir.startswith("linux") and dir not in ["common","qws","features","default"]:
                    pisitools.removeDir(os.path.join(mkspecPath,dir))
        for name in files:
            if name.endswith(".prl"):
                pisitools.dosed(os.path.join(root, name), "^QMAKE_PRL_BUILD_DIR.*", "")

    # Remove useless image directory, images of HTML docs are in doc/html/images
    pisitools.removeDir("%s/src" % qt4.docdir)

    pisitools.dodoc("changes-*", "LGPL_EXCEPTION.txt", "LICENSE.*", "README")
