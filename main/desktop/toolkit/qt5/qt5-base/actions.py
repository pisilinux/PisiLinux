#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

import os

#WorkDir = "qtbase-opensource-src-5.4.1"

qtbase = qt5.prefix

#Temporary bindir to avoid qt4 conflicts
bindirQt5="/usr/lib/qt5/bin"

def setup():
    filteredCFLAGS = get.CFLAGS().replace("-g3", "-g")
    filteredCXXFLAGS = get.CXXFLAGS().replace("-g3", "-g")

    vars = {"PISILINUX_CC" :       get.CC(),
            "PISILINUX_CXX":       get.CXX(),
            "PISILINUX_CFLAGS":    filteredCFLAGS,
            "PISILINUX_LDFLAGS":   get.LDFLAGS()}

    for k, v in vars.items():
        pisitools.dosed("mkspecs/common/g++-base.conf", k, v)
        pisitools.dosed("mkspecs/common/g++-unix.conf", k, v)

    shelltools.export("CFLAGS", filteredCFLAGS)
    shelltools.export("CXXFLAGS", filteredCXXFLAGS)
    #check that dosed commands without releated patches
    pisitools.dosed("mkspecs/common/gcc-base-unix.conf", "\-Wl,\-rpath,")
    pisitools.dosed("mkspecs/common/gcc-base.conf", "\-O2", filteredCFLAGS)
    pisitools.dosed("mkspecs/common/gcc-base.conf", "^(QMAKE_LFLAGS\s+\+=)", r"\1 %s" % get.LDFLAGS())

    autotools.rawConfigure("-no-pch \
                   -opengl es2 \
                   -xcb \
                   -no-webkit2 \
                   -confirm-license \
                   -optimized-qmake \
                   -nomake tests \
                   -no-rpath \
                   -release \
                   -shared \
                   -accessibility \
                   -dbus-linked \
                   -fontconfig \
                   -glib \
                   -gtkstyle \
                   -icu \
                   -disable-static \
                   -c++11 \
                   -system-harfbuzz \
                   -openssl-linked \
                   -system-libjpeg \
                   -system-libpng \
                   -system-sqlite \
                   -system-zlib \
                   -plugin-sql-sqlite \
                   -plugin-sql-odbc \
                   -plugin-sql-psql \
                   -plugin-sql-ibase \
                   -no-sql-tds \
                   -I/usr/include/firebird/ \
                   -I/usr/include/postgresql/server/ \
                   -prefix /usr \
                   -bindir /usr/lib/qt5/bin \
                   -archdatadir /usr/lib/qt5 \
                   -datadir /usr/share/qt5 \
                   -libdir /usr/lib \
                   -docdir /usr/share/doc/qt5 \
                   -sysconfdir /etc/xdg \
                   -xkb-config-root /usr/share/X11/xkb \
                   -no-warnings-are-errors \
                   -no-use-gold-linker") \
                   #")
                   #-opensource \
                   #-reduce-relocations" % (qt5.prefix, bindirQt5, qt5.archdatadir, qt5.libdir, qt5.docdir, qt5.examplesdir, qt5.plugindir, qt5.translationdir, qt5.sysconfdir, qt5.datadir, qt5.importdir, qt5.headerdir))

def build():
    #shelltools.export("LD_LIBRARY_PATH", "%s/lib:%s" % (get.curDIR(), get.ENV("LD_LIBRARY_PATH")))
    qt5.make()
    shelltools.system('sed -i "s|/usr/lib/qt/bin/qdoc|${QTDIR}/qtbase/bin/qdoc|g" qmake/Makefile.qmake-docs')
    shelltools.system('sed -i "s|/usr/lib/qt/bin/qhelpgenerator|${QTDIR}/qttools/bin/qhelpgenerator|g" qmake/Makefile.qmake-docs')

def install():
    pisitools.dodir(qt5.libdir)
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())

    #I hope qtchooser will manage this issue
    for bin in shelltools.ls("%s/usr/lib/qt5/bin" % get.installDIR()):
        pisitools.dosym("/usr/lib/qt5/bin/%s" % bin, "/usr/bin/%s-qt5" % bin)

    mkspecPath = "%s/mkspecs" %  qt5.archdatadir

    pisitools.remove("/usr/lib/*.prl")

    pisitools.dodoc("LGPL_EXCEPTION.txt", "LICENSE.*")
