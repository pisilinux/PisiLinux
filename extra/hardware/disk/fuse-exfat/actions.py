#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get


def build():
    scons.make('CCFLAGS="%s -std=c99"'
                % get.CFLAGS())
    
def install():
    pisitools.dobin("fuse/mount.exfat-fuse")
    pisitools.doman("fuse/mount.exfat-fuse.8")

    pisitools.dodoc("ChangeLog", "COPYING")
