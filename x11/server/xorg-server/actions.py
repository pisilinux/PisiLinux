# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
#    shelltools.chmod("hw/vnc/symlink-vnc.sh")

    autotools.autoreconf("-fiv")
    autotools.configure("--enable-install-libxf86config \
                         --enable-aiglx \
                         --enable-glx-tls \
                         --enable-composite \
                         --enable-record \
                         --enable-dri \
                         --enable-dri2 \
                         --enable-config-udev \
                         --disable-config-dbus \
                         --disable-config-hal \
                         --enable-xfree86-utils \
                         --enable-xorg \
                         --disable-xcliplist \
                         --enable-vnc \
                         --enable-dmx \
                         --enable-xvfb \
                         --disable-xnest \
                         --enable-kdrive \
                         --enable-xephyr \
                         --disable-xfake \
                         --disable-xfbdev \
                         --disable-devel-docs \
                         --without-doxygen \
                         --with-pic \
                         --without-dtrace \
                         --with-int10=x86emu \
                         --with-os-name=\"Pardus\" \
                         --with-os-vendor=\"TÜBİTAK, UEKAE\" \
                         --with-builderstring=\"Package: %s\" \
                         --with-fontrootdir=/usr/share/fonts \
                         --with-default-font-path=catalogue:/etc/X11/fontpath.d,built-ins \
                         --with-xkb-output=/var/lib/xkb \
                         --with-dri-driver-path=/usr/lib/xorg/modules/dri \
                         --without-xmlto \
                         --without-fop \
                         --localstatedir=/var \
                         PCI_TXT_IDS_DIR=/usr/share/X11/pci \
                         " % get.srcTAG())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/etc/X11/fontpath.d")
    pisitools.dodir("/etc/X11/xorg.conf.d")
    pisitools.dodir("/usr/share/X11/pci")
    pisitools.dodir("/usr/share/X11/xorg.conf.d")

    # Remove empty dir
    pisitools.removeDir("/var/log")

    pisitools.dodoc("COPYING", "README")
