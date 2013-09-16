#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-pluggable-dialogs \
                         --enable-sound-settings \
                         --enable-xrandr \
                         --enable-libnotify \
                         --enable-gio-unix \
                         --enable-libxklavier \
                         --enable-xcursor")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "BUGS", "ChangeLog*", "NEWS", "README", "TODO")
