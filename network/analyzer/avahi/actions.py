#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.autoreconf("-fi")
    # --with-systemdsystemunitdir=/lib/systemd/system
    autotools.configure("--with-distro=none \
                         --disable-monodoc \
                         --disable-static \
                         --disable-xmltoman \
                         --disable-qt3 \
                         --disable-qt4 \
                         --disable-doxygen-doc \
                         --disable-gtk3 \
                         --enable-introspection \
                         --enable-mono \
                         --enable-compat-howl \
                         --enable-compat-libdns_sd \
                         --with-systemdsystemunitdir=/lib/systemd/system \
                         --with-avahi-user=avahi \
                         --with-avahi-group=avahi \
                         --with-autoipd-user=avahi-autoipd \
                         --with-autoipd-group=avahi-autoipd \
                         --with-avahi-priv-access-group=avahi")

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