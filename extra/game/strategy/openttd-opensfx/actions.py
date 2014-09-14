#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # set up INSTALL_DIR
    pisitools.dosed("Makefile.local", "^(INSTALL_DIR\s+=)", r"\1 %s/usr/share/openttd/data" % get.installDIR())
    # verbose mode
    pisitools.dosed("Makefile.local", "^#\s(_[EV]\s=\s)@(.*)", r"\1\2")

def build():
    autotools.make()

def install():
    autotools.rawInstall()
    pisitools.dodoc("opensfx-%s/*.txt" % get.srcVERSION())