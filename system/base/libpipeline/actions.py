#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    #who knows pisitools.dosed :)
    cmd="sed -i '/gets is a security hole/d' gnulib/lib/stdio.in.h"
    shelltools.system(cmd)
    autotools.configure("--disable-static \
                         --disable-rpath")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "NEWS", "README")
