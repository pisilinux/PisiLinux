#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("\
                         --sbindir=/sbin \
                         --with-udev-rules-dir=/lib/udev/rules.d \
                         --disable-alsaconf \
                         --disable-maintainer-mode \
                         --disable-rpath \
                        ")

def build():
    autotools.make()
    shelltools.system("cd alsactl")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "README", "TODO", "seq/aconnect/README.aconnect", "seq/aseqnet/README.aseqnet")
