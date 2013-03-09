#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "lirc-%s" % get.srcVERSION().replace("_", "-")
ldflags = get.LDFLAGS().replace("-Wl,-O1", "")

def setup():
    shelltools.export("LDFLAGS", ldflags)
    autotools.autoreconf("-vfi")
    pisitools.dosed("configure*", "portaudio.h", "PORTAUDIO_DISABLED")
    pisitools.dosed("configure*", "vga.h", "SVGALIB_DISABLED")

    # we will use it
    pisitools.dosed("contrib/irman2lirc", "/usr/local/etc/", "/etc/")

    autotools.configure("--localstatedir=/var \
                         --enable-sandboxed \
                         --enable-shared \
                         --disable-static \
                         --disable-debug \
                         --disable-dependency-tracking \
                         --with-transmitter \
                         --with-x \
                         --with-driver=userspace \
                         --with-syslog=LOG_DAEMON")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dobin("contrib/irman2lirc")

    # needed for lircd pid
    pisitools.dodir("/run/lirc")

    # example configs
    pisitools.insinto("/etc", "contrib/lircd.conf", "lircd.conf")
    pisitools.insinto("/etc", "contrib/lircmd.conf", "lircmd.conf")

    pisitools.dohtml("doc/html/*.html")
    pisitools.rename("/%s/%s" % (get.docDIR(), get.srcNAME()), "lirc")

    pisitools.insinto("/%s/lirc/images" % get.docDIR(), "doc/images/*")
    pisitools.insinto("/%s/lirc/contrib" % get.docDIR(), "contrib/*")
    pisitools.insinto("/lib/udev/rules.d", "contrib/lirc.rules", "10-lirc.rules")

