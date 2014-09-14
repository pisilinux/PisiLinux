# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

shelltools.export("HOME",get.workDIR())

def setup():
    libtools.libtoolize()
    autotools.aclocal("-I m4")
    autotools.autoreconf("-vif")
    autotools.configure("--sysconfdir=/etc/snort \
                         --enable-zlib \
                         --enable-gre \
                         --enable-mpls \
                         --enable-targetbased \
                         --enable-ppm \
                         --enable-perfprofiling \
                         --enable-active-response \
                         --enable-normalizer \
                         --enable-reload \
                         --enable-react \
                         --enable-flexresp3 \
                         --enable-shared-rep \
                         --disable-react \
                         --enable-non-ether-decoders \
                         --enable-ha \
                         --disable-corefiles \
                         --with-daq-libraries=/usr/lib/ \
                         --with-daq-includes=/usr/include \
                         --enable-gdb \
                         --enable-inline-init-failopen \
                         --enable-linux-smp-stats \
                         --enable-side-channel \
                         --enable-control-socket")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.move("%s/rules" % get.workDIR(),"%s/etc/snort/rules" % get.installDIR())
    pisitools.dodoc("COPYING", "LICENSE", "RELEASE.NOTES")
