#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static \
                         --enable-pam-module \
                         --localstatedir=/var \
                         --with-systemdsystemunitdir=/lib/systemd/system \
                         --with-pid-file=/run/ConsoleKit/pid")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s/" % get.installDIR())

    pisitools.dodir("/run/ConsoleKit")

    # pam_console-compat
    pisitools.dodir("/run/console")

    pisitools.dodoc("AUTHORS","ChangeLog","README", "COPYING", "HACKING", "NEWS", "TODO")
