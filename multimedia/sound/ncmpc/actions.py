#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")

    autotools.configure("--enable-colors \
                         --enable-lirc")
                         #--enable-lyrics-screen")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "doc/*.sample", "doc/ncmpc.lirc")
