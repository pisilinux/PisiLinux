 #!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.system("NOCONFIGURE=yes ./autogen.sh")
    autotools.configure("--disable-static \
                         --with-x \
                         --libexecdir=/usr/lib/mate-panel \
                         --enable-introspection  \
                         --enable-network-manager  \
                         --disable-deprecation-flags \
                         --disable-scrollkeeper")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
