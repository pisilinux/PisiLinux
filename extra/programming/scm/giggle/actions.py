#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    shelltools.system="./gnome-autogen.sh" 
    #shelltools.system("sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool")
    autotools.rawConfigure("--prefix=/usr")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
     autotools.rawInstall("DESTDIR=%s" % get.installDIR())
     #pisitools.insinto("/usr/include/giggle/", "/include/giggle/giggle-enums.h")
     pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")