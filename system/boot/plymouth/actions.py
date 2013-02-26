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

LOGO_FILE = "/usr/share/pixmaps/plymouth-pardus.png"
THEMEPATH = "/usr/share/plymouth/themes"

def setup():
    autotools.autoreconf("-fis")

    # The end-start colors seems to be used by the two-step plugin
    # Disable nouveau drm renderer as it causes hangs when starting X server
    autotools.configure("--enable-tracing \
                         --with-logo=%s \
                         --with-release-file=/etc/pardus-release \
                         --with-background-color=0x000000 \
                         --with-background-end-color-stop=0x000000 \
                         --with-background-start-color-stop=0x000000 \
                         --with-system-root-install \
                         --with-boot-tty=/dev/tty7 \
                         --with-shutdown-tty=/dev/tty1 \
                         --with-log-viewer \
                         --disable-libdrm_nouveau \
                         --disable-tests \
                         --disable-static \
                         --disable-gdm-transition \
                         --without-rhgb-compat-link \
                         --without-gdm-autostart-file" % LOGO_FILE)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR='%s'" % get.installDIR())

    # Copy necessary files for Charge theme
    pisitools.dodir("%s/charge" % THEMEPATH)
    for f in ("box", "bullet", "entry", "lock"):
        shelltools.copy("%s%s/glow/%s.png" % (get.installDIR(), THEMEPATH, f), "%s%s/charge/" % (get.installDIR(), THEMEPATH))

    # Remove glow theme as it's premature
    pisitools.removeDir("/usr/share/plymouth/themes/glow")

    # Generate initramfs filelist
    #shelltools.system("./generate-flist %s" % get.installDIR())

    pisitools.dodoc("TODO", "COPYING", "README", "ChangeLog")
