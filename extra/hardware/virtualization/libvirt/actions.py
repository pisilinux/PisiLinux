#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    for f in ["src/Makefile.am", "src/Makefile.in", "daemon/Makefile.am", "daemon/Makefile.in"]:
        pisitools.dosed(f, "\$\(localstatedir\)(\/run\/libvirt)", "\\1")
    for f in ["daemon/libvirtd.c", "daemon/libvirtd.conf", "daemon/test_libvirtd.aug.in"]:
        pisitools.dosed(f, "\/var(\/run\/libvirt)", "\\1")
    for f in ["src/locking/virtlockd.pod.in", "src/virtlockd.8.in", "daemon/libvirtd.8.in", "daemon/libvirtd.pod.in", ]:
        pisitools.dosed(f, "LOCALSTATEDIR(\/run\/libvirt)", "\\1")
    autotools.configure("--with-init-script=none \
                         --with-remote-pid-file=/run/libvirtd.pid \
                         --with-qemu-user=qemu \
                         --with-qemu-group=qemu \
                         --with-lxc \
                         --with-udev \
                         --with-qemu \
                         --with-sasl \
                         --with-audit \
                         --with-numactl \
                         --with-yajl \
                         --with-avahi \
                         --with-netcf \
                         --with-libssh2=/usr/lib \
                         --with-capng \
                         --with-polkit \
                         --with-python \
                         --with-network \
                         --with-libvirtd \
                         --with-storage-fs \
                         --with-storage-scsi \
                         --with-storage-mpath \
                         --with-storage-disk \
                         --with-storage-lvm \
                         --without-vbox \
                         --without-vmware \
                         --without-esx \
                         --without-storage-iscsi \
                         --without-hal \
                         --without-xen \
                         --without-phyp \
                         --without-uml \
                         --without-openvz \
                         --without-selinux \
                         --without-apparmor \
                         --disable-static")

def build():
    autotools.make()

#def check():
 #   for v in ["XDG_HOME", "XDG_CACHE_HOME", "XDG_CONFIG_HOME"]:
  #      shelltools.export(v, get.workDIR())
   # autotools.make("check")


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("AUTHORS", "NEWS", "README*", "ChangeLog")
