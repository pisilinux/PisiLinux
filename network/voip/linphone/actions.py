#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --disable-static \
                         --enable-ipv6 \
                         --enable-video \
                         --enable-alsa \
                         --disable-artsc \
                         --disable-strict \
                         --libexecdir=/usr/lib/linphone \
                         --enable-external-mediastreamer \
                         --enable-external-ortp \
                         --enable-zrtp")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gnome")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
