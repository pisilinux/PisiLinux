# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure("--with-app-defaults-dir=/usr/share/X11/app-defaults")
    shelltools.system("xmkmf")

def build():
    autotools.make("includes")
    autotools.make("CDEBUGFLAGS='%s'" % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s install.man" % get.installDIR())

    pisitools.dodoc("ChangeLog", "README", "TODO", "*.ad")
