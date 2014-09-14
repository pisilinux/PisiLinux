#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = ["/usr/sbin/bitlbee"]

def setup():
    autotools.configure("--ssl=gnutls \
                         --otr=0 \
                         --jabber=1 \
                         --yahoo=1 \
                         --oscar=1 \
                         --msn=1 \
                         --twitter=1\
                         --purple=0\
                         --plugins=1\
                         --etcdir=/etc/bitlbee \
                         --datadir=/usr/share/bitlbee")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.insinto("/etc/bitlbee", "bitlbee.conf")
    pisitools.insinto("/etc/xinetd.d", "doc/bitlbee.xinetd", "bitlbee")
    pisitools.insinto("%s/%s/examples/" % (get.docDIR(), get.srcNAME()), "utils/*")

    pisitools.dodir("/var/lib/bitlbee")
    shelltools.chmod("%s/var/lib/bitlbee" % get.installDIR(), 0755)

    pisitools.dohtml("doc/user-guide/user-guide.html")

    pisitools.dodoc("doc/AUTHORS", "doc/CHANGES", "doc/FAQ", "doc/CREDITS", "doc/README", "doc/user-guide/user-guide.txt")
