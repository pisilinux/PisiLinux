#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))

MODULES = "idmap_ad,idmap_rid,idmap_adex,idmap_hash,idmap_tdb2,\
pdb_tdbsam,pdb_ldap,pdb_ads,pdb_smbpasswd,pdb_wbc_sam,pdb_samba4,\
auth_unix,auth_wbc,auth_server,auth_netlogond,auth_script,auth_samba4"


def setup():
    pisitools.flags.add("-D_FILE_OFFSET_BITS=64", "-D_GNU_SOURCE", "-DLDAP_DEPRECATED", "-fPIC")

    autotools.configure("--disable-rpath-install \
                         --enable-fhs \
                         --libdir=/usr/lib \
                         --with-dnsupdate \
                         --with-ads \
                         --with-acl-support \
                         --with-automount \
                         --with-cluster-support \
                         --enable-old-ctdb \
                         --with-dnsupdate \
                         --with-pam \
                         --with-pam_smbpass \
                         --with-quotas \
                         --with-sendfile-support \
                         --with-syslog \
                         --with-swat \
                         --with-utmp \
                         --with-winbind \
                         --with-cachedir=/var/lib/samba \
                         --with-lockdir=/var/lib/samba \
                         --with-piddir=/run/samba \
                         --with-sockets-dir=/run/samba \
                         --with-privatedir=/var/lib/samba/private \
                         --with-logfilebase=/var/log/samba \
                         --with-configdir=/etc/samba \
                         --with-modulesdir=/usr/lib/samba \
                         --with-pammodulesdir=/lib/security \
                         --with-shared-modules=%s \
                        " % MODULES)

def build():
    shelltools.system("make")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosym("samba-4.0/libsmbclient.h", "/usr/include/libsmbclient.h")
