#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make()
    autotools.make("busybox.links")

def install():
    pisitools.insinto("/bin", "busybox.links")
    pisitools.insinto("/bin", "busybox")
