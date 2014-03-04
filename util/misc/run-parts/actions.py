#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--prefix=/usr")

def build():
    autotools.make("run-parts")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #remove conflicting which and man pages
    pisitools.remove("/usr/share/man/*/man1/which.1")
    pisitools.remove("/usr/share/man/man1/which.1")
    pisitools.remove("/usr/bin/which")