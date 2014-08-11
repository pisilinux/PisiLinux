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
    autotools.autoreconf("-if")
    autotools.configure("--disable-static           \
                         --disable-scrollkeeper     \
                         --disable-schemas-compile  \
                         --with-gtk=2.0")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")


def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # remove needless gsettings convert file to avoid slow session start
    pisitools.removeDir("/usr/share/MateConf")
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")