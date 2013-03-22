#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

SAMBA_SOURCE = "source3"

def setup():
    shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE -DLDAP_DEPRECATED -fPIC" % get.CFLAGS())

    # Manually fix manpages
    pisitools.dosed("docs/manpages/*", "\$LOCKDIR", "/run/samba")
    shelltools.cd(SAMBA_SOURCE)

    # Build VERSION
    shelltools.system("script/mkversion.sh")
    shelltools.system("./autogen.sh")
    pisitools.dosed("configure", "(LDSHFLAGS=\")", r"\1%s " % get.LDFLAGS() )
    autotools.configure("--with-dnsupdate \
                         --with-ads \
                         --with-acl-support \
                         --with-automount \
                         --with-dnsupdate \
                         --with-libsmbclient \
                         --with-libsmbsharemodes \
                         --with-mmap \
                         --with-pam \
                         --with-pam_smbpass \
                         --with-quotas \
                         --with-sendfile-support \
                         --with-syslog \
                         --with-utmp \
                         --with-vfs \
                         --with-winbind \
                         --without-smbwrapper \
                         --with-lockdir=/var/lib/samba \
                         --with-piddir=/run \
                         --with-privatedir=/var/lib/samba/private \
                         --with-logfilebase=/var/log/samba \
                         --with-libdir=/usr/lib \
                         --with-configdir=/etc/samba \
                         --with-pammodulesdir=/lib/security \
                         --with-swatdir=/usr/share/swat \
                         --with-shared-modules=idmap_ad,idmap_rid,idmap_adex,idmap_hash,idmap_tdb2 \
                         --with-cluster-support=auto \
                         --with-libtalloc=no \
                         --enable-external-libtalloc=yes \
                         --with-libtdb=no \
                         --with-nmbdsocketdir=/run/nmbd \
                         --disable-smbtorture4")

    pisitools.dosed("Makefile", "^\svfs_examples", deleteLine = True)

def build():
    shelltools.cd(SAMBA_SOURCE)
    shelltools.system("make everything")
    shelltools.cd("../examples/VFS")
    autotools.autoreconf("-fiv")
    autotools.configure()
    shelltools.system("make")

def install():
    shelltools.cd(SAMBA_SOURCE)
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-everything")

    pisitools.insinto("/usr/lib/pkgconfig", "pkgconfig/*pc")

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

    # cups support
    pisitools.dodir("/usr/lib/cups/backend")
    pisitools.dosym("/usr/bin/smbspool", "/usr/lib/cups/backend/smb")

    # directory things
    pisitools.dodir("/var/spool/samba")
    shelltools.chmod("%s/var/spool/samba" % get.installDIR(), 01777)

    pisitools.dodir("/var/log/samba")
    pisitools.dodir("/run/samba")
    pisitools.dodir("/run/winbindd")
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
