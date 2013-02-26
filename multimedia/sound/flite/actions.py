#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "flite-%s-release" % get.srcVERSION()

def setup():
    autotools.configure("--enable-shared \
                         --with-audio=alsa")

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "README")
