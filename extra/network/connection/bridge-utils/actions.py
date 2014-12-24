#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.autoconf()
    autotools.configure("--prefix=/usr \
                         --datarootdir=/usr/share \
                         --with-linux-headers=/usr/include \
                         --sbindir=/usr/bin \
                         --sysconfdir=/etc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # autotools.install('SUBDIRS="brctl doc"')

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "README", "doc/FAQ", "doc/HOWTO")
