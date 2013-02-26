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

def setup():
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-vfi")

    autotools.configure("--with-init-script=none \
                         --with-remote-pid-file=/var/run/libvirtd.pid \
                         --with-qemu-user=qemu \
                         --with-qemu-group=qemu \
                         --with-lxc \
                         --with-udev \
                         --with-qemu \
                         --with-sasl \
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

def check():
#    # Disable broken tests
#    for test in ("daemon-conf",):
#        shelltools.unlink("tests/%s" % test)
#        shelltools.echo("tests/%s" % test, "#!/bin/sh\nexit 0\n")
#        shelltools.chmod("tests/%s" % test, 0755)
    autotools.make("check")


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("AUTHORS", "NEWS", "README*", "ChangeLog")
