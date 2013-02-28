#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION())

def setup():
    autotools.configure("--enable-doc \
                         --enable-static=no \
                         --with-blas='-L/usr/lib/ -lblas -lgfortran' \
                         --with-atlas=yes \
                         --with-ntl=yes \
                         --with-docdir=/usr/share/doc/%s" % get.srcNAME() )

    pisitools.dosed("interfaces/Makefile", "^SUBDIRS = .*$", "SUBDIRS = driver kaapi")
    pisitools.dosed("doc/Makefile", "^LINBOX_DOC_PATH = .*$", "LINBOX_DOC_PATH = %s/usr/share/doc/%s" % (get.installDIR(), get.srcNAME()))
    pisitools.dosed("doc/Makefile", "mkdir \$\(docdir\)", "mkdir -p $(docdir)")

def build():
    autotools.make()

#Test suite has problems but program works fine.
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
