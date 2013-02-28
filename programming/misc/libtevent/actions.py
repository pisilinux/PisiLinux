#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "tevent-%s" % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/lib/*.a")

    # Create symlinks for so file
    pisitools.dosym("libtevent.so.%s" % get.srcVERSION(), "/usr/lib/libtevent.so.%s" % get.srcVERSION().split(".")[0])
    pisitools.dosym("libtevent.so.%s" % get.srcVERSION(), "/usr/lib/libtevent.so")
