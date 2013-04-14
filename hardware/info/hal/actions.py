#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    # NOTE: The acpi stuff should be disabled once we have full upower
    # support. The disk stuffs (umount-helper, eject) should be disabled
    # once we have full udisks support.
    autotools.configure("--exec-prefix=/usr \
                         --localstatedir=/var \
                         --disable-static \
                         --disable-docbook-docs \
                         --disable-gtk-doc \
                         --disable-dependency-tracking \
                         --disable-smbios \
                         --disable-console-kit \
                         --disable-policy-kit \
                         --disable-acl-management \
                         --disable-acpi-ibm \
                         --disable-parted \
                         --disable-sonypic \
                         --without-keymaps \
                         --without-usb-csr \
                         --without-cpufreq \
                         --without-dell-backlight \
                         --without-deprecated-keys \
                         --enable-acpi-acpid \
                         --enable-acpi-proc \
                         --enable-man-pages \
                         --enable-umount-helper \
                         --with-eject=/usr/bin/eject \
                         --with-hal-user=hal \
                         --with-hal-group=hal \
                         --with-udev-prefix=/lib")

    # Disable rpath
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Needed for hal's new cache infrastructure
    pisitools.dodir("/var/cache/hald")

    # Fix permissions of HAL directories
    for d in ["cache", "run"]:
        shelltools.chmod("%s/var/%s/hald" % (get.installDIR(), d), mode=0700)

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "HACKING")
