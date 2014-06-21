# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("%s/crontabs" % get.installDIR())
    libtools.libtoolize("--force --install")
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-yesterday \
                    	--enable-install-isag \
                    	--enable-install-cron \
                    	--enable-copy-only \
                    	--disable-man-group")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc/sysstat", "cron/sysstat.crond")
