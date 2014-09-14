#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-ipv6 \
                         --enable-ssl \
                         --with-socks \
                         --with-textui \
                         --with-bot \
                         --with-proxy")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib/irssi/modules/libirc_proxy.a")
    perlmodules.removePodfiles()
