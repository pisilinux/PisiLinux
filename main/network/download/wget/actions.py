#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-rpath \
                         --with-ssl=openssl")

def build():
    autotools.make()

def install():
    autotools.install()
    
    # default root certs location
    shelltools.echo("%s/etc/wgetrc" % get.installDIR(), "ca_certificate=/etc/ssl/certs/ca-certificates.crt")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog*", "NEWS", "README", "MAILING-LIST")
