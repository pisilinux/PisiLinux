#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--disable-schemas-compile \
                         --with-gtk=2.0")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # remove needless gsettings convert file to avoid slow session start
    pisitools.removeDir("/usr/share/MateConf")
    
    #pisitools.remove("/usr/share/man/man1/mate-notification-properties.1")
    pisitools.removeDir("/usr/share/man/")
