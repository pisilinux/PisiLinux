# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-vif")

    # Disable device node creation during build/install
    pisitools.dosed("util/Makefile.in", "mknod", "echo Disabled: mknod ")

    autotools.configure("--disable-static \
                         --disable-rpath \
                         --enable-lib \
                         --enable-util \
                         --exec-prefix=/ \
                         --bindir=/bin")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/dev")
    pisitools.removeDir("/etc")

    # Make compat symlinks into /usr/bin
    pisitools.dosym("/bin/fusermount", "/usr/bin/fusermount")
    pisitools.dosym("/bin/ulockmgr_server", "/usr/bin/ulockmgr_server")

    # Move pkgconfig file to /usr/lib
    pisitools.domove("/lib/pkgconfig", "/usr/lib/")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "FAQ", "Filesystems", "NEWS", "README", "README.NFS")
