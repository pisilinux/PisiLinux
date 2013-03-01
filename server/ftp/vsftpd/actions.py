#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    autotools.make('CC="%s" CFLAGS="%s -fpie" LINK="-pie -lssl" LDFLAGS="%s"' % (get.CC(),get.CFLAGS(),get.LDFLAGS()))

def install():
    pisitools.dosbin("vsftpd")

    pisitools.dodir("/home/ftp")
    pisitools.dodir("/home/ftp/incoming")
    pisitools.dodir("/usr/share/vsftpd/empty")
    pisitools.dodir("/var/log/vsftpd")

    pisitools.newdoc("vsftpd.conf", "vsftpd.conf.example")
    pisitools.doman("vsftpd.conf.5", "vsftpd.8")
    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "SECURITY")
    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "EXAMPLE")
    pisitools.dodoc("AUDIT", "BENCHMARKS", "BUGS", "Changelog", "FAQ",\
                    "LICENSE", "README*", "REFS", "REWARD", "SIZE", \
                    "SPEED", "TODO", "TUNING")
