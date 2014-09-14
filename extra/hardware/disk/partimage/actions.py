#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")

    autotools.configure("--docdir=%s/%s/%s \
                         --disable-static \
                         --enable-gui-qt \
                         --enable-gui-newt \
                         --enable-gui-text \
                         --enable-ssl \
                         --enable-nls \
                         --enable-pam" % (get.installDIR(), get.docDIR(), get.srcNAME()))

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("BUGS", "AUTHORS", "ABOUT-NLS", "COPYING", "THANKS")
    pisitools.dodoc("ChangeLog", "FORMAT", "README", "README.partimaged")
