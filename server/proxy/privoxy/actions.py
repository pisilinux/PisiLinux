#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-stable" % get.srcDIR()

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-dynamic-pcre \
                         --enable-zlib \
                         --with-user=privoxy \
                         --with-group=privoxy \
                         --without-docbook \
                         --without-db2html")

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/sbin", "privoxy")
    pisitools.doman("privoxy.1")

    pisitools.dodir("/etc/privoxy/templates")
    pisitools.insinto("/etc/privoxy", "*.action")
    pisitools.insinto("/etc/privoxy", "config")
    pisitools.insinto("/etc/privoxy", "default.filter")
    pisitools.insinto("/etc/privoxy", "trust")
    pisitools.insinto("/etc/privoxy/templates", "templates/*")

    pisitools.dodir("/var/log/privoxy")
