#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -fvisibility=hidden" % get.CFLAGS())
shelltools.export("LDFLAGS", "%s -fvisibility=hidden" % get.LDFLAGS())

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")

    autotools.configure("--disable-static \
                         --enable-shared \
                         --enable-pam \
                         --disable-rpath \
                         --disable-device-hal \
                         --disable-mount-hal \
                         --enable-device-udev \
                         --enable-mount-udisks \
                         --enable-mount-eeze \
                         --enable-elementary \
                         --enable-emotion \
                         --enable-enotify \
                         --enable-ephysics \
                         --disable-wayland-clients \
                         --enable-conf-wallpaper2 \
                         --disable-illume2 \
                         --disable-doc")

    shelltools.system("patch -p1 < backround-default.patch")
    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/enlightenment/data/themes/","%s/*.edj" % get.workDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "README")
