#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

flags = get.CXXFLAGS().replace("-fstack-protector", "").replace("-O2", "")

def setup():
    pisitools.dosed("ttf.cpp", "freetype/", "freetype2/")
    #FIXME: find who is to blame...
    shelltools.sym(".", ".libs")

    pisitools.dosed("Makefile", r"^(LDFLAGS=)(.+)$", r"\1%s \2" % get.LDFLAGS())

def build():
    autotools.make('CXX="%s" \
                    OPTFLAGS="%s" \
                    DEBUG="" \
                    -j1' % (get.CXX(), flags))

def install():
    pisitools.dobin("ttmkfdir")

    pisitools.dodoc("README")
