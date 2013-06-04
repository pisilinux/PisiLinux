#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-debug")

def build():
    autotools.make()

def install():
    pisitools.insinto("/etc", "mozpluggerrc")    
    pisitools.insinto("/usr/bin", "mozplugger-controller")
    pisitools.insinto("/usr/bin", "mozplugger-helper")
    pisitools.insinto("/usr/bin", "mozplugger-linker")
    pisitools.insinto("/usr/lib/mozilla/plugins", "mozplugger.so")
    pisitools.insinto("/usr/share/man/man7", "mozplugger.7")

    pisitools.dodoc("COPYING")
