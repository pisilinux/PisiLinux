#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-demos \
                         --disable-docs")
    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")
    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.install()

    #pisitools.removeDir("/usr/share/gtkmm-2.4")
    pisitools.removeDir("/usr/share/devhelp")

    pisitools.dodoc("ChangeLog","COPYING", "PORTING", "NEWS", "README")
