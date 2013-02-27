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
    shelltools.export("LIBASSUAN_CONFIG", "/usr/bin/libassuan-config")
    shelltools.export("LDAPLIBS", "-lldap -llber")
    autotools.configure("--exec-prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())

    pisitools.dodoc("AUTHORS", "THANKS", "COPYING", "README", "NEWS", "TODO")
