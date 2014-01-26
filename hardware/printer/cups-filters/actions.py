# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("configure", "localstatedir/run/cups", "localstatedir/cups")
    autotools.configure("--prefix=/usr  \
                         --sysconfdir=/etc \
                         --sbindir=/usr/bin \
                         --with-rcdir=no \
                         --localstatedir=/run \
                         --enable-avahi \
                         --with-browseremoteprotocols=DNSSD,CUPS \
                         --with-test-font-path=/usr/share/fonts/TTF/DejaVuSans.ttf")

def build():
    autotools.make()
    
#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
