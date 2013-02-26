#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

# FIXME: libpulsedsp.la should be added, but it doesn't build on our system
emul32_libs = "libpulsecommon-%s.la \
               libpulse.la \
               libpulse-simple.la \
               libpulse-mainloop-glib.la" % get.srcVERSION()

def setup():
    # Disable as-needed for now as it doesn't compile
    # Lennart has introduced a circular dep in the libraries. libpulse requires
    # libpulsecommon but libpulsecommon requires libpulse.
    shelltools.export("LDFLAGS", "%s -Wl,--no-as-needed" % get.LDFLAGS())

    autotools.autoreconf("-fi")
    libtools.libtoolize()

    options = "--disable-dependency-tracking \
               --disable-static \
               --disable-rpath \
               --disable-hal \
               --disable-jack \
               --with-system-user=pulse \
               --with-system-group=pulse \
               --with-access-group=pulse-access"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                     --libexecdir=/usr/lib32 \
                     --disable-gconf \
                     --disable-gtk2 \
                     --disable-jack \
                     --disable-bluez \
                     --disable-asyncns \
                     --disable-lirc \
                     --disable-x11 \
                     --disable-oss-output \
                     --disable-oss-wrapper \
                     --disable-solaris \
                     --disable-manpages \
                     --disable-samplerate \
                     --disable-default-build-tests"
        shelltools.export("CC", "%s -m32" % get.CC())

    autotools.configure(options)


def build():
    if get.buildTYPE() == "emul32":
        autotools.make("-C src %s" % emul32_libs)
        return

    #autotools.make("LIBTOOL=/usr/bin/libtool")
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

    # Needed for service.py
    pisitools.dodir("/var/run/pulse")
    pisitools.dodir("/var/lib/pulse")

    # HAL is no longer supported by default
    pisitools.removeDir("/etc/dbus-1")

    pisitools.dodoc("README", "LICENSE", "GPL", "LGPL")
    pisitools.dohtml("doxygen/html/*")

