#!    pisitools.remove("bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #shelltools.export("LDFLAGS", "%s -lm" % get.LDFLAGS())
    shelltools.system("./autogen.sh --prefix=/usr \
				    --sysconfdir=/etc \
				    --localstatedir=/var \
				    --disable-static \
				    --disable-scrollkeeper \
				    --enable-gnucat \
				    --disable-startup-notification \
				    --enable-unique ")    
    

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())