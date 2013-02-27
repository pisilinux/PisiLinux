#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir='tuxmath_w_fonts-%s' % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/applications", "tuxmath.desktop")
    pisitools.dosym("/usr/share/tuxmath/images/icons/icon.png", "/usr/share/pixmaps/tuxmath.png")

    pisitools.dodoc( "doc/COPYING_GPL3", "doc/TODO", "doc/README", "doc/OFL", "doc/changelog")
