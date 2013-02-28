#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="plt-%s" % get.srcVERSION()

def setup():
    shelltools.export("LDFLAGS","")

    shelltools.cd("src")
    autotools.configure("--enable-mred \
                         --enable-shared \
                         --enable-lt=/usr/bin/libtool \
                         --enable-backtrace \
                         --enable-perl \
                         --enable-gl \
                         --enable-libpng \
                         --enable-libjpeg \
                         --enable-cairo")

def build():
    shelltools.cd("src")
    autotools.make()

def install():
    shelltools.cd("src")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.doman("../man/man1/*")
    pisitools.dodoc("../readme.txt","README")
    pisitools.domove("/usr/share/plt/doc/*","/usr/share/doc/%s" % get.srcNAME())
    pisitools.removeDir("/usr/share/plt")

    pisitools.dosym("/usr/lib/plt", "/usr/share/plt")
    pisitools.dosym("/usr/share/doc/%s" % get.srcNAME(), "/usr/lib/plt/doc")
