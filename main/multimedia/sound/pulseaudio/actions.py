#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

# FIXME: libpulsedsp.la should be added, but it doesn't build on our system
emul32_libs = "libpulsecommon-%s.la \
               libpulse.la \
               libpulse-simple.la \
               libpulse-mainloop-glib.la \
              " % get.srcVERSION()

def setup():
    options = "--prefix=/usr         \
               --sysconfdir=/etc     \
               --localstatedir=/var  \
               --libexecdir=/usr/libexec \
               --disable-dependency-tracking \
               --disable-static \
               --disable-rpath \
               --disable-jack \
               --disable-systemd \
               --disable-bluez4 \
               --disable-oss-output \
               --enable-largefile \
               --with-system-user=pulse \
               --with-system-group=pulse \
               --with-access-group=pulse-access \
               --with-database=tdb \
               --with-module-dir=/usr/lib/pulse/modules \
               --with-udev-rules-dir=/lib/udev/rules.d"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                     --libexecdir=/usr/lib32 \
                     --disable-gconf \
                     --disable-gtk2 \
                     --disable-jack \
                     --disable-bluez4 \
                     --disable-bluez5 \
                     --disable-asyncns \
                     --disable-lirc \
                     --disable-x11 \
                     --disable-oss-output \
                     --disable-oss-wrapper \
                     --disable-solaris \
                     --disable-manpages \
                     --disable-samplerate \
                     --disable-default-build-tests"

    shelltools.echo(".tarball-version", get.srcVERSION())
    #shelltools.system("NOCONFIGURE=1 ./bootstrap.sh")
    autotools.configure(options)

    pisitools.dosed("libtool", "CC(\s-shared\s)", r"CC -Wl,-O1,--as-needed\1")

def build():
    if get.buildTYPE() == "emul32":
        autotools.make("-C src %s" % emul32_libs)
        return

    autotools.make()

    #generate html docs
    autotools.make("doxygen")

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("-C src \
                              lib_LTLIBRARIES=\"%s\" \
                              DESTDIR=%s" % (emul32_libs, get.installDIR()),
                             "install-libLTLIBRARIES")
        autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-pkgconfigDATA")
        return

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Disable autospawn by default
    shelltools.system("sed -e '/autospawn/iautospawn=yes' -i '%s/etc/pulse/client.conf'" % get.installDIR())
    # Speed up pulseaudio shutdown
    # Lower resample quality, saves CPU
    shelltools.system("sed -e '/exit-idle-time/iexit-idle-time=0' \
                       -e '/resample-method/iresample-method=speex-float-0' \
                       -i '%s/etc/pulse/daemon.conf'" % get.installDIR())

    # Needed for service.py
    pisitools.dodir("/run/pulse")
    pisitools.dodir("/var/lib/pulse")

    # HAL is no longer supported by default
    pisitools.removeDir("/etc/dbus-1")

    pisitools.dodoc("README", "LICENSE", "GPL", "LGPL")
    pisitools.dohtml("doxygen/html/*")
