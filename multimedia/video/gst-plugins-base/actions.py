#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

def setup():
    pisitools.dosed("configure.ac", "AM_CONFIG_HEADER", "AC_CONFIG_HEADERS")
    autotools.autoreconf("-vfi")
    opts = {
            "introspection": "no" if get.buildTYPE() == "emul32" else "yes",
            "gnome-vfs": "dis" if get.buildTYPE() == "emul32" else "en"
           }
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --disable-examples \
                         --%(gnome-vfs)sable-gnome-vfs \
                         --enable-libvisual \
                         --enable-experimental \
                         --enable-introspection=%(introspection)s \
                         --with-package-name='PisiLinux gstreamer-plugins-base package' \
                         --with-package-origin='http://www.pisilinux.org' \
                        " % opts)

def build():
    autotools.make()

# tests fail sandbox
#def check():
#    autotools.make("-C tests/check check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
