#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    options = "--with-xml=expat \
               --with-system-pid-file=/run/dbus/pid \
               --with-system-socket=/run/dbus/system_bus_socket \
               --with-console-auth-dir=/run/console/ \
               --with-session-socket-dir=/tmp \
               --with-dbus-user=dbus \
               --disable-selinux \
               --disable-static \
               --disable-tests \
               --disable-asserts \
               --disable-doxygen-docs \
               --disable-xml-docs"

    if get.buildTYPE() == "emul32":
        # Build only libdbus
        pisitools.dosed("Makefile.am", "(.*SUBDIRS=dbus) .*", "\\1")

    autotools.autoreconf("-vif")
    autotools.configure(options)

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32": return
    pisitools.removeDir("/var/run")

    # needs to exist for the system socket
    pisitools.dodir("/run/dbus")
    pisitools.dodir("/var/lib/dbus")
    pisitools.dodir("/usr/share/dbus-1/services")

    pisitools.dodoc("AUTHORS", "ChangeLog", "HACKING", "NEWS", "README", "doc/TODO", "doc/*.txt")
    pisitools.dohtml("doc/")
