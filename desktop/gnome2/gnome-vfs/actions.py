#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # hmmm, we should do the hal mounting with gnome-mount?
    autotools.autoreconf("-fi")
    autotools.configure("--disable-selinux \
                         --disable-static \
                         --enable-samba --with-samba-includes=/usr/include/samba-4.0 \
                         --disable-hal --enable-avahi --disable-howl")
    
    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    shelltools.export("GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL", "1")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("TODO", "NEWS", "README", "HACKING", "AUTHORS", "ChangeLog")
