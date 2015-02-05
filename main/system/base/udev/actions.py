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
    autotools.autoreconf("-fi")
    libtools.libtoolize("--force")

    options = " ac_cv_header_sys_capability_h=yes \
                --prefix=/usr \
                --sysconfdir=/etc \
                --bindir=/bin%s \
                --sbindir=/sbin%s \
                --docdir=/usr/share/doc/udev \
                --libdir=/usr/lib%s \
                --libexecdir=/usr/libexec \
                --with-html-dir=/usr/share/doc/udev/html \
                --with-rootlibdir=/lib%s \
                --with-rootprefix= \
                --disable-selinux \
                --enable-gudev \
                --enable-split-usr \
                --disable-gtk-doc-html \
                --enable-rule_generator \
                --with-modprobe=/sbin/modprobe \
                --enable-keymap \
                --enable-blkid \
                --enable-split-usr \
                --disable-manpages \
               " % ((suffix, )*4)

    options += "\
                --disable-static \
                --disable-gtk-doc \
                --enable-introspection=no \ \
               " if get.buildTYPE() == "emul32" else \
               "\
                --enable-static \
                --enable-libkmod \
                --enable-introspection=yes \
               "
    shelltools.export("BLKID_CFLAGS", "-I/tools/include")
    shelltools.export("BLKID_LIBS", "-L/tools/lib -lblkid")            
    shelltools.system("sed -r -i 's|/usr(/bin/test)|\1|' test/udev-test.pl")

    shelltools.system("sed -i -e '/--enable-static is not supported by systemd/s:as_fn_error:echo:' configure")
    autotools.configure(options)

def build():
    shelltools.echo("Makefile.extra", "BUILT_SOURCES: $(BUILT_SOURCES)")
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    autotools.make("-f Makefile -f Makefile.extra")
    targets = " \
                src/libudev \
                src/gudev \
                src/udev \
                src/ata_id \
                src/cdrom_id \
                src/collect \
                src/scsi_id \
                src/v4l_id \
                src/accelerometer \
               "

    autotools.make(targets)

    autotools.make("-C docs/libudev")
    autotools.make("-C docs/gudev")

#~def check():
#~    autotools.make("check")
#~ 

def install():

    autotools.rawInstall("-j1 DESTDIR=%s%s" % (get.installDIR(), suffix))
    if get.buildTYPE() == "emul32":
        shelltools.move("%s%s/lib%s" % (get.installDIR(), suffix, suffix), "%s/lib%s" % (get.installDIR(), suffix))
        shelltools.move("%s%s/usr/lib%s" % (get.installDIR(), suffix, suffix), "%s/usr/lib%s" % (get.installDIR(), suffix))
#~         for f in shelltools.ls("%s/usr/lib32/pkgconfig" % get.installDIR()):
#~             pisitools.dosed("%s/usr/lib32/pkgconfig/%s" % (get.installDIR(), f), "emul32", "usr")
        #shelltools.unlinkDir("%s%s" % (get.installDIR(), suffix))
        return
    # Create needed directories
    for d in ("", "net", "pts", "shm", "hugepages"):
         pisitools.dodir("/lib/udev/devices/%s" % d)

    # Create vol_id and scsi_id symlinks in /sbin probably needed by multipath-tools
    pisitools.dosym("/lib/udev/scsi_id", "/sbin/scsi_id")

    # Create /sbin/systemd-udevd -> /sbin/udevd sysmlink, we need it for MUDUR, do not touch this sysmlink.
    # Mudur needs this symlink as well
    #pisitools.dosym("/bin/udevadm", "/sbin/udevadm")

    # Create /etc/udev/rules.d for backward compatibility
    pisitools.dodir("/etc/udev/rules.d")

    pisitools.dodir("/run/udev")
    pisitools.dodoc("README")

    # Add man files
    #pisitools.doman("man/systemd.link.5", "man/udev.7", "man/udevadm.8", "man/systemd-udevd.service.8")
