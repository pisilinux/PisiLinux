#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--enable-jit \
                         --enable-pcretest-libreadline \
                         --enable-pcre32 \
                         --enable-pcre16 \
                         --enable-utf \
                         --enable-unicode-properties \
                         --enable-cpp \
                         --docdir=/%s/%s \
                         --disable-static" % (get.docDIR(), get.srcNAME()))

def build():
    autotools.make()

def check():
    autotools.make("-j1 check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
