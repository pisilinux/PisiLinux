# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.system("make -f client.mk build")

def install():
    shelltools.cd("../obj-kompozer")
    
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())
    
    pisitools.dodoc("dist/bin/LICENSE")