#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("CC=%s" %get.CC())

def install():
    #rename netcat binary to differentiate it from gnu version
    pisitools.insinto("/usr/bin/", "nc", "netcat-openbsd")
    #insert a symlink as nc so that applications expecting nc command can run it
    pisitools.dosym("./netcat-openbsd", "/usr/bin/nc")

    # copy the man stuff and create a symlink for both command possibilities
    pisitools.doman("nc.1")
    pisitools.dosym("./nc.1", "/usr/share/man/man1/netcat-openbsd.1")
