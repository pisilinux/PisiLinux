#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    shelltools.touch("ChangeLog")
    autotools.autoreconf("-fi")
    autotools.configure("--with-libcap-ng=yes \
                         --enable-drivedb \
                         --with-systemdsystemunitdir=/lib/systemd/system")

def build():
    autotools.make("CXXFLAGS='%s -fpie'" % get.CXXFLAGS())

def install():
    pisitools.dosed("smartd.service","sysconfig/smartmontools","conf.d/smartd")
    pisitools.dosed("smartd.service","smartd_opts","SMARTD_ARGS")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "NEWS", "README", "WARNINGS", "smartd.conf")
