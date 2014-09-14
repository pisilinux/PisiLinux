#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure('--enable-interfaces="c,cxx"')
def build():
    autotools.make()

# tests run hours and hours, running it is left to packager
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("BUGS", "COPYING", "CREDITS", "ChangeLog", "STANDARDS", "TODO", "README*", "NEWS")
