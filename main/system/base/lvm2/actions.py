#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def builddiet():
    pisitools.flags.add("-fno-lto")
    shelltools.export("LIBS","-lpthread -luuid")
    #dietCC = "diet %s %s %s -Os -static" % (get.CC(), get.CFLAGS(), get.LDFLAGS())
    dietCC = "%s %s %s -Os -static" % (get.CC(), get.CFLAGS(), get.LDFLAGS())
    shelltools.export("CC", dietCC)
    
    autotools.make("distclean")

    autotools.autoreconf("-fi")
    autotools.configure('ac_cv_lib_dl_dlopen=no \
                         --with-staticdir="/sbin" \
                         --enable-debug \
                         --with-optimisation=\"%s -Os\" \
                         --enable-static_link \
                         --with-lvm1=internal \
                         --disable-readline \
                         --disable-nls \
                         --disable-selinux \
                         --with-confdir=/etc \
                         --enable-applib     \
                         --enable-cmdlib     \
                         --enable-pkgconfig  \
                         --enable-udev_rules \
                         --with-systemdsystemunitdir=no \
                         --enable-udev_sync' % get.CFLAGS())

    pisitools.dosed("lib/misc/configure.h","rpl_malloc","malloc")
    pisitools.dosed("lib/misc/configure.h","rpl_realloc","realloc")

    autotools.make("-j1 -C include")
    autotools.make("-j1 -C lib LIB_SHARED= VERSIONED_SHLIB=")
    autotools.make("-j1 -C libdm LIB_SHARED= VERSIONED_SHLIB=")
    autotools.make("-j1 -C libdaemon LIB_SHARED= VERSIONED_SHLIB=")
    autotools.make("-j1 -C tools dmsetup.static lvm.static DIETLIBC_LIBS=\"-lcompat\"")

    pisitools.insinto("/usr/lib/dietlibc/lib-i386", "libdm/ioctl/libdevmapper.a")
    pisitools.insinto("/sbin/", "tools/lvm.static")
    pisitools.insinto("/sbin/", "tools/dmsetup.static")


def setup():
    # Breaks linking when sandbox is disabled
    shelltools.export("CLDFLAGS", get.LDFLAGS())

    shelltools.export("LIB_PTHREAD", "-lpthread")
    pisitools.dosed("conf/example.conf.in", "use_lvmetad = 0", "use_lvmetad = 1")

    autotools.autoreconf("-fi")
    autotools.configure("--enable-lvm1_fallback \
                         --with-default-pid-dir=/run \
                         --with-default-run-dir=/run/lvm \
                         --with-default-locking-dir=/run/lock/lvm \
                         --with-dmeventd-path=/sbin/dmeventd \
                         --enable-fsadm \
                         --with-pool=internal \
                         --with-user= \
                         --with-group= \
                         --with-usrlibdir=/usr/lib \
                         --with-usrsbindir=%s \
                         --with-udevdir=/lib/udev/rules.d \
                         --with-device-uid=0 \
                         --with-device-gid=6 \
                         --with-device-mode=0660 \
                         --enable-dmeventd \
                         --enable-udev_rules \
                         --enable-udev_sync \
                         --with-snapshots=internal \
                         --with-mirrors=internal \
                         --with-interface=ioctl \
                         --enable-static_link=no \
                         --disable-readline \
                         --disable-realtime \
                         --disable-selinux \
                         --with-confdir=/etc \
                         --enable-applib \
                         --enable-cmdlib \
                         --enable-pkgconfig " % get.sbinDIR())

#    pisitools.dosed("make.tmpl","-lm","")

def build():
    autotools.make("-C include")
    #autotools.make("-C libdm")
    #autotools.make("-C lib")
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())

    for dir in ["archive", "backup", "cache"]:
        pisitools.dodir("/etc/lvm/%s" % dir)
        shelltools.chmod(get.installDIR() + "/etc/lvm/%s" % dir, 0700)

    #pisitools.move("/sbin/lvmconf","scripts/lvmconf.sh")

    builddiet()
    pisitools.dodoc("COPYING", "COPYING.LIB", "README", "VERSION", "VERSION_DM", "WHATS_NEW", "WHATS_NEW_DM")
