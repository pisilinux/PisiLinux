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

    autotools.configure("--with-python \
                         --without-ldap \
                         --with-popt \
                         --disable-rpath \
                         --enable-gtk-doc-html=no \
                         --disable-gtk-doc")
    
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

    autotools.make("-C po update-gmo")

def install():
    autotools.rawInstall("DESTDIR='%s'" % get.installDIR())
    
    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("ABOUT*", "AUTHORS", "COPYING", "NEWS", "README")
