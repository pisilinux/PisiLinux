#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def build():
    autotools.make("SUBDIRS=mozilla")


def install():
    pisitools.dodir("usr/share/ca-certificates/mozilla")
    pisitools.dodir("usr/sbin")

    autotools.install("SUBDIRS=mozilla DESTDIR=%s" % get.installDIR())
    pisitools.doman("sbin/update-ca-certificates.8")

    shelltools.cd("%s/usr/share/ca-certificates" % get.installDIR())
    shelltools.system("find . -name '*.crt' | sort | cut -b3- > ca-certificates.conf")
    pisitools.insinto("/etc/", "ca-certificates.conf")

    pisitools.dodir("/etc/ca-certificates/update.d")
    pisitools.dodir("etc/ssl/certs")
