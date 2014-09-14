#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s -C man-pages-posix-2003-a" % get.installDIR())

    # These come from attr
    pisitools.remove("/usr/share/man/man2/flistxattr.2")
    pisitools.remove("/usr/share/man/man2/removexattr.2")
    pisitools.remove("/usr/share/man/man2/fgetxattr.2")
    pisitools.remove("/usr/share/man/man2/fsetxattr.2")
    pisitools.remove("/usr/share/man/man2/lsetxattr.2")
    pisitools.remove("/usr/share/man/man2/lremovexattr.2")
    pisitools.remove("/usr/share/man/man2/listxattr.2")
    pisitools.remove("/usr/share/man/man2/getxattr.2")
    pisitools.remove("/usr/share/man/man2/setxattr.2")
    pisitools.remove("/usr/share/man/man2/llistxattr.2")
    pisitools.remove("/usr/share/man/man2/fremovexattr.2")
    pisitools.remove("/usr/share/man/man2/lgetxattr.2")

    # These come from libcap
    pisitools.remove("/usr/share/man/man2/capget.2")
    pisitools.remove("/usr/share/man/man2/capset.2")

    # Comes from xorg-input
    pisitools.remove("/usr/share/man/man4/mouse.4")

    pisitools.dodoc("man-pages-*.Announce", "README")
