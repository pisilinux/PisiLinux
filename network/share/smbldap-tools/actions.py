#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #pisitools.dosed("smbldap_tools.pm", "/etc/opt/IDEALX/", "/etc/smbldap-tools/")
    pisitools.dosed("smbldap.conf", "/etc/opt/IDEALX/", "/etc/smbldap-tools/")
    #pisitools.dosed("smbldap_tools.pm", "/opt/IDEALX/", "/etc/smbldap-tools/")
    pisitools.dosed("smbldap.conf", "/opt/IDEALX/", "/etc/smbldap-tools/")

    # Set SSL certs directory
    pisitools.dosed("smbldap.conf", "/etc/pki/tls/certs/", "/etc/ssl/certs/")

    # Generate manpages
    for f in shelltools.ls("smbldap-*"):
        shelltools.system("pod2man --section=8 %s > doc/%s.8" % (f, f))

def install():
    pisitools.dosbin("smbldap-*")
    pisitools.remove("/usr/sbin/smbldap-tools.spec")

    #pisitools.insinto("/usr/lib/perl5/vendor_perl/%s/" % get.curPERL(), "smbldap_tools.pm")

    pisitools.dodir("/etc/smbldap-tools")
    pisitools.insinto("/etc/smbldap-tools", "smbldap.conf")
    pisitools.insinto("/etc/smbldap-tools", "smbldap_bind.conf")

    pisitools.dodoc("CONTRIBUTORS", "COPYING", "ChangeLog", "FILES", "INFRA", \
                    "README", "TODO")

    pisitools.doman("doc/*.8")
