#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.unlink("py-compile" )
    shelltools.sym("/bin/true", "py-compile")

    autotools.configure("--disable-mime-install \
                         --enable-packager-mode")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "README","NEWS","FAQ","TODO")

