#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-bsdtar \
                         --disable-bsdcpio")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")    

def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/share/man/man5/tar.5")
    pisitools.remove("/usr/share/man/man5/cpio.5")
    pisitools.remove("/usr/share/man/man5/mtree.5")

    # Remove empty dirs
    os.removedirs("%s/usr/share/man/man1" % get.installDIR())
    os.removedirs("%s/usr/bin" % get.installDIR())

    pisitools.dodoc("COPYING","NEWS","README")
