#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/lib/firmware", "ivtv-firmware")
    
    pisitools.removeDir("/usr/include")
    pisitools.remove("/usr/local/bin/v4l2-ctl")
 
    pisitools.dodoc("ChangeLog", "COPYING", "README")

