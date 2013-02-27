#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "crystalhd"

def build():
    #libcrystalhd and crystalhd-firmware
    shelltools.cd('linux_lib/libcrystalhd')
    autotools.make('clean')
    autotools.make()

def install():
    pisitools.dodoc('COPYING')
    #libcrystalhd and crystalhd-firmware
    shelltools.cd('linux_lib/libcrystalhd')
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
