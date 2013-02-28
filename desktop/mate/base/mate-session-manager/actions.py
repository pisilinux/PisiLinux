 #!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())
def setup():
    shelltools.system("./autogen.sh --prefix=/usr \
				    --sysconfdir=/etc \
				    --localstatedir=/var \
				    --libexecdir=/usr/lib \
				    --enable-splash \
				    --with-mateconf-source='xml::/etc/mateconf/mateconf.xml.defaults' \
				    --with-default-wm='marco' \
				    --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
