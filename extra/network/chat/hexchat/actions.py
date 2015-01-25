#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.configure(" --prefix=/usr \
                          --enable-{dbus,perl,python='python2.7',textfe,fishlim,doat,sysinfo,minimal-flags}")

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    pisitools.domo("po/tr.po", "tr", "hexchat.mo")
    autotools.rawInstall("DESTDIR='%s' \
               	          UPDATE_ICON_CACHE=true \
                          UPDATE_MIME_DATABASE=true \
                          UPDATE_DESKTOP_DATABASE=true" % get.installDIR())
    #shelltools.cd("share/doc")
    pisitools.dodoc("COPYING", "readme.*")
