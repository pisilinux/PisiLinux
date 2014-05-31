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
    shelltools.export("AUTOPOINT", "true")
    pisitools.dosed("autogen.sh", "tool_run.*autopoint --force.*")
    
    pisitools.dosed("ext/modplug/gstmodplug.cc", "stdafx.h", "libmodplug/stdafx.h")

    shelltools.export("NOCONFIGURE", "1")
    shelltools.system("./autogen.sh")

    autotools.configure("--disable-static \
                         --disable-examples \
                         --disable-gtk-doc \
                         --disable-rpath \
                         --with-package-name='PisiLinux gstreamer-plugins-bad package' \
                         --with-package-origin='http://www.pisilinux.org' \
                         --disable-experimental \
                         --disable-assrender")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")


def build():
    autotools.make()

#FIXME: tests now tries to 
#def check():
#    # for sandbox violations
#    shelltools.export("HOME", get.workDIR())
#    autotools.make("-C tests/check check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README", "RELEASE", "REQUIREMENTS")

