#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Those are in gentoo ebuild too, but what are they for?
    # I couldn't find in docs, some comment would be helpful here -gurer
    shelltools.export("SANEI_JPEG", "sanei_jpeg.o")
    shelltools.export("SANEI_JPEG_LO", "sanei_jpeg.lo")

    autotools.autoreconf("-fi")

    autotools.configure("--enable-ipv6 \
                         --enable-avahi \
                         --enable-libusb \
                         --disable-rpath \
                         --disable-locking \
                         --disable-latex \
                         --with-docdir=/usr/share/doc/%s \
                         --with-gphoto2" % get.srcNAME())
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Install udev rule
    pisitools.insinto("/lib/udev/rules.d", "tools/udev/libsane.rules", "65-libsane.rules")

    # Add epson epkowa and brother2 backends also
    shelltools.echo("%s/etc/sane.d/dll.conf" % get.installDIR(),
                    "# Epson 'epkowa' backend\n" +
                    "# See http://www.sane-project.org/cgi-bin/driver.pl?manu=Epson&bus=any for supported scanners\n" +
                    "# In order to use this backend, you have to install iscan package\nepkowa")

    shelltools.echo("%s/etc/sane.d/dll.conf" % get.installDIR(),
                    "\n# Brother backend\n" +
                    "# See http://en.pardus-wiki.org/Brother_scanner_support_for_DCP_and_MFC_models for installation\n" +
                    "brother\nbrother2\nbrother3")

    shelltools.echo("%s/etc/sane.d/dll.conf" % get.installDIR(), "\n# Added for Xerox Phaser 3100 MFP\nXeroxPhaser3100\n")


