#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

srcversion = get.srcVERSION()

def build():
    autotools.make()
    
    shelltools.system("find . -name '*.crt' | sort | cut -b3- > ca-certificates.conf")

def install():
    pisitools.insinto("/usr/bin/", "sbin/update-ca-certificates")
    pisitools.doman("sbin/update-ca-certificates.8")
    pisitools.insinto("/usr/share/ca-certificates/cacert.org/", "cacert.org/*.crt")
    pisitools.insinto("/usr/share/ca-certificates/mozilla/", "mozilla/*.crt")
    pisitools.insinto("/usr/share/ca-certificates/spi-inc.org/", "spi-inc.org/*.crt")
    
    pisitools.insinto("/etc/", "ca-certificates.conf")
    
    pisitools.dodir("/etc/ca-certificates/update.d/")
