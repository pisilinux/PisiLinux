#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # hmmm, we should do the hal mounting with gnome-mount?
    autotools.autoreconf("-fi")
    autotools.configure("--disable-selinux \
                         --disable-static \
                         --disable-schemas-install \
                         --with-hal-mount=/usr/bin/mount \
                         --with-hal-umount=/usr/bin/umount \
                         --with-hal-eject=/usr/bin/eject")

def build():
    #shelltools.export("GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL", "1")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("TODO", "NEWS", "README", "HACKING", "AUTHORS", "ChangeLog")
