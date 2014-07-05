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
                        --mandir=/usr/share/man \
                        --enable-install-isag \
                        --enable-install-cron \
                        --enable-copy-only \
                        --disable-man-group")

def build():
    autotools.make("-j1")

def install():    
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.makedirs("/usr/lib/systemd/system/")
    shelltools.makedirs("%s/etc/cron.daily/" % get.installDIR())
    shelltools.makedirs("%s/etc/cron.hourly/" % get.installDIR())
    
    pisitools.insinto("/usr/lib/systemd/system/", "sysstat.service")
    pisitools.insinto("/usr/lib/systemd/system/", "cron/sysstat-summary.timer")
    pisitools.insinto("/usr/lib/systemd/system/", "cron/sysstat-collect.service")
    pisitools.insinto("/usr/lib/systemd/system/", "cron/sysstat-collect.timer")
    pisitools.insinto("/usr/lib/systemd/system/", "cron/sysstat-summary.service")
    
    pisitools.insinto("/etc/sysstat", "cron/sysstat.crond")
    
    pisitools.remove("sysstat*")