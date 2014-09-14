#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4

# if pisi can't find source directory, see /var/pisi/tomahawk/work/ and:
# WorkDir="tomahawk-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    kde4.configure("-DBUILD_BUILD_RELEASE=on \
                    -DBUILD_WITH_QT4=on \
                    -DBUILD_WITH_KDE4=on \
                    -DBUILD_BUILD_TESTS=off \
                    -DCMAKE_INSTALL_PREFIX=/usr \
                    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
                    -DCMAKE_INSTALL_LIBEXECDIR=lib/")
    #pisitools.dosed("build/CMakeCache.txt", "CMAKE_INSTALL_LIBDIR:PATH=lib64", "CMAKE_INSTALL_LIBDIR:PATH=lib")

def build():
    kde4.make()

def install():
    kde4.install("DESTDIR=%s" % get.installDIR())

# Take a look at the source folder for these file as documentation.
#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("tomahawk")

# You can use these as variables, they will replace GUI values before build.
# Package Name : tomahawk
# Version : 0.8.0
# Summary : Tomahawk, the social music player app (Qt / C++)

# For more information, you can look at the Actions API
# from the Help menu and toolbar.

# By PiSiDo 2.0.0
