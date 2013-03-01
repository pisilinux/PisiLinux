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
    shelltools.copy("/usr/share/libtool/config/config.sub", "%s/libtar-1.2.11/autoconf/" % get.workDIR())
    shelltools.copy("/usr/share/libtool/config/ltmain.sh", "%s/libtar-1.2.11/autoconf/" % get.workDIR())
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
