# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("\
                         --disable-static \
                         --disable-silent-rules \
                         --with-udev-rules-dir=/lib/udev/rules.d \
                         --enable-debug \
                        ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/lib/udev/rules.d")
    pisitools.removeDir("/usr/lib/systemd")
    pisitools.dodoc("AUTHORS", "ChangeLog", "GPL", "README")
