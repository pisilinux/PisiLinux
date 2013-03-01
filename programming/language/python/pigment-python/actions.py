#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static\
                        --prefix=%s/usr" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "AUTHORS", "TODO", "NEWS", "ChangeLog")
