#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.system("bash ./bootStrap.bash")
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.insinto("/", "install/usr")

    #shelltools.cd("../plugins/build")
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #shelltools.cd("../../")
    pisitools.insinto("/usr/share/pixmaps", "avidemux_icon.png", "avidemux.png")

    # remove windows exe and dll files
    #pisitools.removeDir("/usr/share/ADM_addons")

    pisitools.dodoc("COPYING", "AUTHORS", "License*")
    pisitools.doman("man/*")
