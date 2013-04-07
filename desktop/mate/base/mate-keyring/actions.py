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
    shelltools.system("./autogen.sh  --disable-static \
				     --with-gtk=2.0 \
				     --enable-pam \
				     --prefix=/usr \
				     --sysconfdir=/etc \
				     --disable-static \
				     --localstatedir=/var \
				     --libexecdir=/usr/lib/mate-keyring \
				     --with-pam-dir=/lib/security \
				     --with-root-certs=/etc")        
        
         

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README", "NEWS", "AUTHORS", "ChangeLog")