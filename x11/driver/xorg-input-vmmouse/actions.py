# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "xf86-input-vmmouse-%s" % get.srcVERSION()

def setup():
    autotools.configure("--with-xorg-conf-dir==/usr/share/X11/xorg.conf.d")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/lib/hal")
    pisitools.removeDir("/usr/share/hal")
