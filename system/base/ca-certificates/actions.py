#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    autotools.make("SUBDIRS=mozilla")
    
    shelltools.cd("mozilla")
    shelltools.system("find . -name '*.crt' | sort | cut -b3- > ../ca-certificates.conf")

def install():
    pisitools.dodir("usr/share/ca-certificates/mozilla")
    pisitools.dodir("usr/sbin")
    
    autotools.install("SUBDIRS=mozilla DESTDIR=%s" % get.installDIR())
    pisitools.doman("sbin/update-ca-certificates.8")
      
    pisitools.insinto("/etc/", "ca-certificates.conf")
    
    pisitools.dodir("/etc/ca-certificates/update.d")
    pisitools.dodir("etc/ssl/certs")
