#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


WorkDir = "./"

def setup():
    shelltools.move("README.mkinitramfs", "README")

def install():
    pisitools.dodir("/etc/initramfs.d")
    pisitools.dodoc("README")

