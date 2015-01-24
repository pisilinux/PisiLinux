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
    autotools.configure("--prefix=/usr \
                          --enable-python \
                          --enable-shm \
                          --enable-spell='libsexy' \
                          --enable-textfe")

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")
    
def build():
    autotools.make()

def install():
    pisitools.domo("po/tr.po", "tr", "hexchat.mo")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("share/doc")
    #pisitools.dodoc("COPYING", "readme.*")
