#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # We take the module "spirit" from boost 1.55 and use it instead of the one
    # that is provided by boost 1.56+ because hugin doesn't compile with the
    # latter.  This is no proper fix for the problem but it works for now.
    shelltools.copytree("%s/boost_1_55_0/boost/spirit" % get.workDIR(), "src/boost")

    # See https://gcc.gnu.org/bugzilla/show_bug.cgi?id=61214#c5
    # and https://www.mail-archive.com/debian-bugs-dist@lists.debian.org/msg1231921.html.
    # for why the "-fno-devirtualize" flag is needed.  I can go away with GCC 4.9.2+.
    pisitools.cxxflags.add("-fno-devirtualize")

    shelltools.system("LIBS=-lboost_signals LDFLAGS=-lboost_signals")

    cmaketools.configure("-Wcpp -DCMAKE_BUILD_TYPE=Release \
                          -DwxWidgets_CONFIG_EXECUTABLE=/usr/bin/wxconfig \
                          -DENABLE_LAPACK=yes")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("AUTHORS", "README", "TODO")
