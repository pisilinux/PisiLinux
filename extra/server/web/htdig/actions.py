#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="htdig-3.2.0b6"

def setup():
    autotools.configure("--enable-shared \
                         --disable-static \
                         --enable-tests \
                         --enable-bigfile \
                         --with-config-dir=/etc/htdig \
                         --with-common-dir=/var/www/localhost/htdig \
                         --with-database-dir=/var/lib/htdig \
                         --localstatedir=/var/lib/htdig \
                         --with-cgi-bin-dir=/var/www/localhost/cgi-bin \
                         --with-image-dir=/var/www/localhost/htdig \
                         --with-search-dir=/var/www/localhost/htdig \
                         --with-default-config-file=/etc/htdig/htdig.conf \
                         --with-apache=/usr/sbin/apache2 \
                         --with-zlib=/usr \
                         --with-ssl")
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("search.html","/var/www/localhost/htdig/index.html")
    pisitools.dosym("/var/www/localhost/cgi-bin/htsearch", "/usr/bin/htsearch")

    shelltools.chmod("%s/var/www/localhost/htdig/*" % get.installDIR(), 0644)

    pisitools.dosed("%s/etc/htdig/htdig.conf" % get.installDIR(), get.installDIR())
    pisitools.dosed("%s/usr/bin/rundig" % get.installDIR(), get.installDIR())

    pisitools.dosym("/var/www/localhost/htdig","/usr/share/htdig")

    pisitools.remove("/usr/lib/htdig/*.la")
    pisitools.remove("/usr/lib/htdig_db/*.la")
    pisitools.removeDir("/usr/include")
