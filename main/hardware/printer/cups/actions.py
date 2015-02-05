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
    #pisitools.flags.add("-fstack-protector-all", "-DLDAP_DEPRECATED=1")
    pisitools.dosed("config-scripts/cups-sharedlibs.m4", "( -shared )", " -Wl,--as-needed\\1")

    # For --enable-avahi
    autotools.aclocal("-I config-scripts")
    autotools.autoconf("-I config-scripts")

    options = '--with-cups-user=lp \
               --with-cups-group=lp \
               --with-system-groups=lpadmin \
               --with-docdir=/usr/share/cups/html \
               --with-dbusdir=/etc/dbus-1 \
               --with-optim="%s" \
               --with-php=/usr/bin/php-cgi \
               --with-cupsd-file-perm=0755 \
               --with-log-file-perm=0600 \
               --without-java \
               --enable-acl \
               --enable-ssl=yes \
               --enable-libpaper \
               --enable-libusb=yes \
               --enable-debug \
               --enable-avahi \
               --enable-gssapi \
               --enable-dbus \
               --enable-pam=yes \
               --enable-relro \
               --enable-dnssd \
               --enable-browsing \
               --enable-threads \
               --enable-raw-printing \
               --disable-gnutls \
               --disable-launchd \
               --without-rcdir \
               --libdir=/usr/lib \
               --without-perl \
               --with-logdir=/var/log/cups \
               KRB5CONFIG=/usr/bin/krb5-config \
               --localstatedir=/var \
               --with-rundir=/run/cups \
               --with-xinetd=/etc/xinetd.d \
              ' % get.CFLAGS()

    if get.buildTYPE() == "emul32":
        options += '  \
                     --enable-libusb=no \
                     --disable-avahi \
                     --disable-dnssd \
                     --disable-gssapi \
                     --disable-dbus \
                     --bindir=/usr/bin32 \
                     --sbindir=/usr/sbin32 \
                     --libdir=/usr/lib32'

    autotools.configure(options)

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    if get.buildTYPE() == "emul32":
        # SERVERBIN is hardcoded to /usr/lib/cups, thus it overwrites 64 bit libraries
        autotools.rawInstall("BUILDROOT=%s SERVERBIN=%s/usr/serverbin32 install-libs" % (get.installDIR(), get.installDIR()))
        pisitools.domove("/usr/bin32/cups-config", "/usr/bin", "cups-config-32bit")
        pisitools.removeDir("/usr/bin32")
        pisitools.removeDir("/usr/sbin32")
        pisitools.removeDir("/usr/serverbin32")

        # remove files now part of cups-filters
        pisitools.remove("/usr/share/cups/data/testprint")
        pisitools.removeDir("/usr/share/cups/banners")
        pisitools.dodir("/usr/share/cups/banners")
        return

    autotools.rawInstall("BUILDROOT=%s install-headers install-libs install-data install-exec" % get.installDIR())
    shelltools.chmod("%s/run/cups/certs" % get.installDIR(), 0755)

    pisitools.dodir("/usr/share/cups/profiles")

    # Serial backend needs to run as root
    #shelltools.chmod("%s/usr/lib/cups/backend/serial" % get.installDIR(), 0700)

    pisitools.dodoc("CHANGES.txt", "CREDITS.txt", "LICENSE.txt", "README.txt")
