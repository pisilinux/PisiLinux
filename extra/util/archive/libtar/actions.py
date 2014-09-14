#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #libtar-1.2.11-free.patch
    pisitools.dosed("lib/output.c", "#ifdef STDC_HEADERS", "#ifdef STDC_HEADERS\n# include <stdlib.h>")
    pisitools.dosed("lib/wrapper.c", "#ifdef STDC_HEADERS", "#ifdef STDC_HEADERS\n# include <stdlib.h>")
    autotools.autoreconf("-fvi")
    autotools.configure("--disable-static")

    # Remove rpath
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog*", "COPYRIGHT", "README", "TODO")
