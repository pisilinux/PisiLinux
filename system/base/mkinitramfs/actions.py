#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


WorkDir = "./"

def setup():
    shelltools.move("README.mkinitramfs", "README")

def install():
    pisitools.dodir("/etc/initramfs.d")
    pisitools.dodoc("README")

