#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("MONO_SHARED_DIR", get.workDIR())
shelltools.export("XDG_CONFIG_HOME", get.workDIR())

def setup():
    autotools.configure("--enable-subversion \
                         --enable-monoextensions \
                         --enable-gnome-platform \
                         --enable-c \
                         --enable-versioncontrol \
                         --disable-update-mimedb \
                         --disable-update-desktopdb")

def build():
    autotools.make("DESTDIR=%s -j1" % get.installDIR())

def install():
    autotools.install()

    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    # Empty files: NEWS
    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
