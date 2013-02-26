 #!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())
shelltools.export("CFLAGS", "%s" % get.CFLAGS())

def setup():
    shelltools.system("./autogen.sh --prefix=/usr \
				    --localstatedir=/var \
				    --disable-static \
				    --sysconfdir=/etc \
				    --with-x \
				    --libexecdir=/usr/lib/mate-panel \
				    --enable-deprecation-flags \
				    --disable-schemas-install \
				    --disable-scrollkeeper \
				    --enable-introspection \
				    --enable-matecomponent")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
