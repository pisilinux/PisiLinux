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
                         --with-html-dir=/usr/share/doc/%s/html \
                         --with-temp-mount-dir=/run/libgpod \
                         --without-hal \
                         --without-mono \
                         --disable-gtk-doc \
                         --disable-static \
                         --enable-udev \
                        " % get.srcNAME())

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # For temporary mounts
    pisitools.dodir("/run/libgpod")
    
    # rm "/usr/lib/pkgconfig/libgpod-sharp.pc"
    pisitools.remove("/usr/lib/pkgconfig/libgpod-sharp.pc")
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")
