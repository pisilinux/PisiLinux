#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

SAMBA_SOURCE = "source3"

def setup():
    shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE -DLDAP_DEPRECATED -fPIC" % get.CFLAGS())

    # Manually fix manpages
    pisitools.dosed("docs/manpages/*", "\$LOCKDIR", "/var/run/samba")

    shelltools.cd(SAMBA_SOURCE)

    # Build VERSION
    shelltools.system("script/mkversion.sh")
    shelltools.system("./autogen.sh")
    autotools.configure("--with-dnsupdate \
                         --with-ads \
                         --with-acl-support \
                         --with-automount \
                         --with-pam \
                         --with-pam_smbpass \
                         --with-quotas \
                         --with-sys-quotas \
                         --with-sendfile-support \
                         --with-syslog \
                         --with-utmp \
                         --with-fhs \
                         --with-winbind \
                         --with-cluster-support=auto \
                         --with-libtalloc=no \
                         --with-libtdb=no \
                         --sysconfdir=/etc/samba \
                         --localstatedir=/var \
                         --libdir=/usr/lib \
                         --with-configdir=/etc/samba \
                         --with-piddir=/var/run/samba \
                         --with-lockdir=/var/lib/samba \
                         --with-logfilebase=/var/log/samba \
                         --with-pammodulesdir=/lib/security \
                         --with-privatedir=/var/lib/samba/private \
                         --with-swatdir=/usr/share/swat \
                         --with-readline \
                         --with-ldap \
                         --with-cifsmount \
                         --with-cifsumount \
                         --with-cifsupcall \
                         --enable-external-libtalloc=yes \
                         --enable-external-libtdb=yes \
                         --enable-shared=yes \
                         --enable-static=no \
                         --enable-cups \
                         --enable-swat \
                         --with-shared-modules=idmap_rid,idmap_ad,idmap_adex,idmap_hash,idmap_tdb2")

def build():
    shelltools.cd(SAMBA_SOURCE)
    autotools.make("proto")
    autotools.make("everything")

def install():
    shelltools.cd(SAMBA_SOURCE)
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-everything")

    pisitools.insinto("/usr/lib/pkgconfig", "pkgconfig/*pc")

    # we have all mount.* helpers in /usr/bin
    pisitools.domove("/usr/sbin/mount.cifs", "/usr/bin/")
    pisitools.domove("/usr/sbin/umount.cifs", "/usr/bin/")

    # Nsswitch extensions. Make link for wins and winbind resolvers
    pisitools.dolib_so("../nsswitch/libnss_wins.so")
    pisitools.dolib_so("../nsswitch/libnss_winbind.so")
    pisitools.dosym("libnss_wins.so", "/usr/lib/libnss_wins.so.2")
    pisitools.dosym("libnss_winbind.so", "/usr/lib/libnss_winbind.so.2")

    # pam extensions
    pisitools.doexe("bin/pam_smbpass.so", "/lib/security")
    pisitools.doexe("bin/pam_winbind.so", "/lib/security")

    # Move mount helpers to /sbin
    pisitools.dodir("/sbin")

    for f in ("mount.cifs", "umount.cifs"):
        pisitools.domove("/usr/bin/%s" % f, "/sbin")

    pisitools.domove("/usr/sbin/cifs.upcall", "/sbin")

    # Set SUID bit for mount helpers
    shelltools.chmod("%s/sbin/*mount.cifs" % get.installDIR(), mode=04755)

    # cups support
    pisitools.dodir("/usr/lib/cups/backend")
    pisitools.dosym("/usr/bin/smbspool", "/usr/lib/cups/backend/smb")

    # directory things
    pisitools.dodir("/var/spool/samba")
    shelltools.chmod("%s/var/spool/samba" % get.installDIR(), 01777)

    pisitools.dodir("/var/log/samba")
    pisitools.dodir("/var/run/samba")
    pisitools.dodir("/var/run/winbindd")
    pisitools.dodir("/var/cache/samba")

    pisitools.dodir("/var/lib/samba/private")
    pisitools.dodir("/var/lib/samba/winbindd_privileged")
    pisitools.dodir("/var/lib/samba/netlogon")
    pisitools.dodir("/var/lib/samba/profiles")
    pisitools.dodir("/var/lib/samba/printers/W32X86")
    pisitools.dodir("/var/lib/samba/printers/WIN40")
    pisitools.dodir("/var/lib/samba/printers/W32ALPHA")
    pisitools.dodir("/var/lib/samba/printers/W32MIPS")
    pisitools.dodir("/var/lib/samba/printers/W32PPC")

    # Needed by "net usershare" support
    pisitools.dodir("/var/lib/samba/usershares")

    pisitools.dodir("/usr/lib/samba/auth")
    pisitools.dodir("/usr/lib/samba/idmap")

    # Remove conflicting man pages
    pisitools.remove("/usr/share/man/man8/tdb*")

