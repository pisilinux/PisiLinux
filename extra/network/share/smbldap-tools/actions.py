#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def  build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodir("/etc/smbldap-tools")
    pisitools.insinto("/etc/smbldap-tools", "smbldap.conf")
    pisitools.insinto("/etc/smbldap-tools", "smbldap_bind.conf")

    pisitools.dodoc("CONTRIBUTORS", "COPYING", "ChangeLog", "FILES", "INFRA", \
                    "README", "TODO")

    pisitools.doman("*.8")
