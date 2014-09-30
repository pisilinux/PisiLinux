# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pisitools.dosed("Makefile", "MANDIR = /usr/man", "MANDIR = /usr/share/man")
    autotools.make("-C po update-po")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/sbin/ntsysv")
    pisitools.remove("/sbin/chkconfig")
    pisitools.remove("/usr/share/man/man8/chkconfig.8")
    pisitools.remove("/usr/share/man/man8/ntsysv.8")
    pisitools.removeDir("/usr/share/man/man5")

    pisitools.dodoc("COPYING")
