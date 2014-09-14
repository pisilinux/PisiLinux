# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("conf_dir=/etc/conf.d --enable-yesterday \
                        --enable-install-isag \
                        --enable-install-cron \
                        --enable-copy-only \
                        --disable-man-group")

def build():
    autotools.make("-j1")

def install():    
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc/sysstat", "cron/sysstat.crond")
    
    pisitools.remove("sysstat*")