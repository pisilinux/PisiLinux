#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    shelltools.export("LDFLAGS", "%s -lgmodule-2.0" % get.LDFLAGS())
    autotools.make('CC=%s \
                    INSTALLROOT=/usr \
                    INCLUDEDIR=/usr/include/gkrellm2 \
                    LOCALEDIR=/usr/share/locale \
                    STRIP="" \
                    LINK_FLAGS="%s -Wl,-E" \
                    enable_nls=1 \
                    without-ssl=yes \
                    without-sensors=no \
                    without-libsensors=yes' % (get.CC(), get.LDFLAGS()))
                    # without ssl option enables gnutls

def install():
    autotools.rawInstall("DESTDIR=%s \
                          PREFIX=/usr" % get.installDIR())

    pisitools.insinto("/etc", "server/gkrellmd.conf")

    pisitools.doman("gkrellm.1")
    pisitools.doman("gkrellmd.1")

    pisitools.dodoc("CREDITS", "README", "Changelog", "COPYRIGHT")
    pisitools.dohtml("*")


