#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static \
                         --disable-esd \
                         --disable-rpath \
                         --with-package-name='Pardus gstreamer-plugins-good package' \
                         --with-package-origin='http://www.pardus-anka.org' \
                         --disable-schemas-install")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "README", "RELEASE")
