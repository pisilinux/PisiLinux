#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure.ac", "png_check_sig", "png_sig_cmp")
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-glout \
                         --enable-master \
                         --enable-main \
                         --disable-uninstall \
                         --with-x \
                         --disable-etc \
                         --disable-initscripts \
                         --disable-sysinstall \
                         --disable-games")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")

    #We better cleanup
    pisitools.removeDir("/usr/share/armagetronad/desktop")
    shelltools.chmod("%s/etc/armagetronad/rc.config" % get.installDIR(), 0644)
