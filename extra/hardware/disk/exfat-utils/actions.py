#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    scons.make('CCFLAGS="%s -std=c99"'
                % get.CFLAGS())
                

def install():
    pisitools.dobin("mkfs/mkexfatfs")
    pisitools.dobin("dump/dumpexfat")
    pisitools.dobin("fsck/exfatfsck")
    pisitools.dobin("label/exfatlabel")    
    
    pisitools.doman("mkfs/mkexfatfs.8")
    pisitools.doman("dump/dumpexfat.8")
    pisitools.doman("fsck/exfatfsck.8")
    pisitools.doman("label/exfatlabel.8")
    
    pisitools.dodoc("ChangeLog", "COPYING")