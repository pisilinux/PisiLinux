#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

suffix = "32" if get.buildTYPE() == "emul32" else ""

def setup():
    pisitools.flags.add("-fno-lto")
    #shelltools.echo("docs/gtk-doc.make", "EXTRA_DIST=")
    autotools.autoreconf("-fi")
    libtools.libtoolize("--force")

    options = " ac_cv_header_sys_capability_h=yes \
                --bindir=/sbin%s \
                --sbindir=/sbin%s \
                --docdir=/usr/share/doc/udev \
                --libdir=/usr/lib%s \
                --libexecdir=/lib%s/udev \
                --with-firmware-path=/lib%s/firmware/updates:/lib%s/firmware \
                --with-html-dir=/usr/share/doc/udev/html \
                --with-rootlibdir=/lib%s \
                --with-rootprefix= \
                --without-python \
                --disable-xz \
                --disable-nls \
                --disable-pam \
                --disable-dbus \
                --disable-audit \
                --disable-gcrypt \
                --disable-gnutls \
                --disable-logind \
                --disable-polkit \
                --disable-seccomp \
                --disable-selinux \
                --disable-qrencode \
                --disable-readahead \
                --disable-microhttpd \
                --disable-myhostname \
                --disable-quotacheck \
                --disable-python-devel \
                --disable-libcryptsetup \
                --enable-gudev \
                --enable-split-usr \
               " % ((suffix, )*7)

    options += "\
                --disable-acl \
                --disable-kmod \
                --disable-static \
                --disable-manpages \
                --disable-gtk-doc \
                --disable-introspection \
               " if get.buildTYPE() == "emul32" else \
               "\
                --enable-acl \
                --enable-kmod \
                --enable-static \
                --enable-introspection \
               "

    shelltools.system("sed -i -e '/--enable-static is not supported by systemd/s:as_fn_error:echo:' configure")
    autotools.configure(options)

def build():
    shelltools.echo("Makefile.extra", "BUILT_SOURCES: $(BUILT_SOURCES)")
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    autotools.make("-f Makefile -f Makefile.extra")

    targets = " \
                libudev.la \
                libgudev-1.0.la \
                systemd-udevd \
                udevadm \
                ata_id \
                cdrom_id \
                collect \
                scsi_id \
                v4l_id \
                accelerometer \
                mtd_probe \
               "

    autotools.make(targets)

    autotools.make("-C docs/libudev")
    autotools.make("-C docs/gudev")

#~ def check():
    #~ autotools.make("check")
#~ 

def install():
    targets = " install-libLTLIBRARIES \
                install-includeHEADERS \
                install-libgudev_includeHEADERS \
                install-rootbinPROGRAMS \
                install-rootlibexecPROGRAMS \
                install-udevlibexecPROGRAMS \
                install-dist_udevconfDATA \
                install-dist_udevrulesDATA \
                install-girDATA \
                install-pkgconfiglibDATA \
                install-sharepkgconfigDATA \
                install-typelibsDATA \
                install-dist_docDATA \
                libudev-install-hook \
                install-directories-hook \
                install-dist_bashcompletionDATA \
                install-dist_networkDATA \
                rootlibexec_PROGRAMS='systemd-udevd' \
                rootbin_PROGRAMS='udevadm' \
                lib_LTLIBRARIES='libudev.la \
                                 libgudev-1.0.la' \
                pkgconfiglib_DATA='src/libudev/libudev.pc \
                                   src/gudev/gudev-1.0.pc' \
                dist_bashcompletion_DATA='shell-completion/bash/udevadm' \
                dist_network_DATA='network/99-default.link' \
                pkginclude_HEADERS='src/libudev/libudev.h' \
              "

    autotools.make("-j1 DESTDIR=%s%s %s" % (get.installDIR(), suffix, targets))
    if get.buildTYPE() == "emul32":
        shelltools.move("%s%s/lib%s" % (get.installDIR(), suffix, suffix), "%s/lib%s" % (get.installDIR(), suffix))
        shelltools.move("%s%s/usr/lib%s" % (get.installDIR(), suffix, suffix), "%s/usr/lib%s" % (get.installDIR(), suffix))
        for f in shelltools.ls("%s/usr/lib32/pkgconfig" % get.installDIR()):
            pisitools.dosed("%s/usr/lib32/pkgconfig/%s" % (get.installDIR(), f), "emul32", "usr")
        #shelltools.unlinkDir("%s%s" % (get.installDIR(), suffix))
        return
    # Create needed directories
    #for d in ("", "net", "pts", "shm", "hugepages"):
         #pisitools.dodir("/lib/udev/devices/%s" % d)

    # Create vol_id and scsi_id symlinks in /sbin probably needed by multipath-tools
    pisitools.dosym("/lib/udev/scsi_id", "/sbin/scsi_id")

    # Create /sbin/systemd-udevd -> /sbin/udevd sysmlink, we need it for MUDUR, do not touch this sysmlink.
    pisitools.dosym("/sbin/systemd-udevd", "/sbin/udevd")
    pisitools.dosym("/lib/systemd/systemd-udevd", "/sbin/systemd-udevd")
    # Mudur needs this symlink as well
    pisitools.dosym("/bin/udevadm", "/sbin/udevadm")

    # Create /etc/udev/rules.d for backward compatibility
    pisitools.dodir("/etc/udev/rules.d")

    pisitools.dodir("/run/udev")
    pisitools.dodoc("README", "TODO")

    # Add man files
    pisitools.doman("man/systemd.link.5", "man/udev.7", "man/udevadm.8", "man/systemd-udevd.service.8")
