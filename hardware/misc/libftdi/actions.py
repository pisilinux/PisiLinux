#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # I haven't enabled non-C bindings, cause they aren't very useful
    # at the moment. In case if you need them later:
    # C++ binding: remove --without-boost and depend on boost
    autotools.configure("--without-boost \
                         --enable-python-binding \
                         --disable-static")

    # kernel doesn't provide usb_device anymore
    pisitools.dosed("packages/99-libftdi.rules", "usb_device", "usb")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Compiled examples are not useful, they also pollute /usr/bin namespace
    pisitools.remove("/usr/bin/bitbang*")
    pisitools.remove("/usr/bin/find*")
    pisitools.remove("/usr/bin/simple")
    pisitools.remove("/usr/bin/baud_test")
    #pisitools.remove("/usr/bin/serial_read")

    # Their source can be useful though
    pisitools.dodoc("examples/*.c", destDir="%s/examples" % get.srcNAME())

    # Install udev rule
    pisitools.insinto("/lib/udev/rules.d", "packages/99-libftdi.rules")

    pisitools.doman("doc/man/man3/*.3")

    pisitools.dodoc("AUTHORS", "COPYING.LIB", "ChangeLog", "LICENSE", "README")
