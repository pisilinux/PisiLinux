#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

if get.buildTYPE() == "emul32":
    libexec = "/tmp"
    sysconf = "/tmp"
else:
    libexec = "/usr/libexec/at-spi2"
    sysconf = "/etc"

def setup():
    autotools.configure("--disable-static \
                         --disable-xevie \
                         --libexecdir=%s\
                         --with-dbus-daemondir=/usr/bin \
                         --sysconfdir=%s \
                        " % (libexec, sysconf))

    pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
    pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
    pisitools.dosed("libtool","( -shared )", " -Wl,--as-needed\\1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.removeDir("/etc")
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/tmp")
        return

    pisitools.dodoc("AUTHORS", "COPYING", "README", "NEWS")