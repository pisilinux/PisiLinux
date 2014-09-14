#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # force to use python2.x
    pisitools.dosed("configure.ac", "(python)3", "\\1")

    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr \
                         --with-udevdir=/lib/udev")

def build():
    shelltools.system('LANG="en_US.UTF-8" make')

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
