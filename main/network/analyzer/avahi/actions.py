#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("avahi-daemon/avahi-daemon.conf", "^#(disallow-other-stacks=)no", "\\1yes")

    # fix avahi socket path
    pisitools.dosed('configure.ac', '^(avahi_runtime_dir=")\$\{localstatedir\}(\/run")', r'\1\2')

    autotools.autoreconf("-fi")
    # --with-systemdsystemunitdir=/lib/systemd/system
    autotools.configure("\
                         --with-distro=none \
                         --disable-monodoc \
                         --disable-static \
                         --disable-xmltoman \
                         --disable-qt3 \
                         --disable-qt4 \
                         --disable-doxygen-doc \
                         --enable-glib \
                         --enable-gobject \
                         --enable-introspection \
                         --enable-mono \
                         --enable-gtk3 \
                         --enable-compat-howl \
                         --enable-compat-libdns_sd \
                         --with-avahi-user=avahi \
                         --with-avahi-group=avahi \
                         --with-autoipd-user=avahi-autoipd \
                         --with-autoipd-group=avahi-autoipd \
                         --with-avahi-priv-access-group=avahi \
                         --with-dbus-system-address=unix:path=/run/dbus/system_bus_socket \
                        ")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")    

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Add missing symlinks for avahi-compat-howl and avahi-compat-dns-sd
    pisitools.dosym("/usr/lib/pkgconfig/avahi-compat-howl.pc", "/usr/lib/pkgconfig/howl.pc")
    pisitools.dosym("/usr/lib/pkgconfig/avahi-compat-libdns_sd.pc", "/usr/lib/pkgconfig/libdns_sd.pc")
    pisitools.dosym("/usr/include/avahi-compat-libdns_sd/dns_sd.h", "/usr/include/dns_sd.h")

    # Remove example
    pisitools.remove("/etc/avahi/services/sftp-ssh.service")

    pisitools.dodir("/run/avahi-daemon")
    pisitools.dodir("/var/lib/avahi-autoipd")

    pisitools.dodoc("docs/AUTHORS", "docs/README", "docs/TODO")

    pisitools.removeDir("var/run")