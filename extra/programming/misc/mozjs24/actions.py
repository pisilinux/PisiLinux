#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mozjs-%s/js/src" % get.srcVERSION()

def setup():
    shelltools.export("CPPFLAGS", get.CXXFLAGS())
    autotools.configure("--with-system-nspr \
                         --enable-system-ffi \
                         --enable-readline \
                         --enable-threadsafe")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())