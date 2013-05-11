#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("CFLAGS","%s -fpie -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
shelltools.export("LDFLAGS","%s -pie" % get.LDFLAGS())

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-mountconfig \
                         --enable-ipv6 \
                         --enable-nfsv3 \
                         --enable-nfsv4 \
                         --enable-gss \
                         --with-krb5=/usr \
                         --with-statedir=/var/lib/nfs")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/lib/nfs/statd/sm")
    pisitools.dodir("/var/lib/nfs/statd/sm.bak")
    pisitools.dodir("/var/lib/nfs/v4recovery")
    pisitools.dodir("/var/lib/nfs/rpc_pipefs")

    pisitools.insinto("/etc", "utils/mount/nfsmount.conf")

    pisitools.domove("/usr/sbin/rpc.statd", "/sbin/")
