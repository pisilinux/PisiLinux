#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import qt4

def setup():
    kde4.configure('-DCMAKE_INSTALL_LIBDIR=lib \
                    -DCMAKE_BUILD_TYPE=Release \
                    -DCMAKE_SKIP_RPATH=ON')

def build():
    kde4.make()

def install():
    kde4.install()

    #Also add symlink for qt-only applications
    pisitools.dosym("%s/plugins/phonon_backend/phonon_vlc.so" % kde4.modulesdir, "%s/phonon_backend/libphonon_vlc.so" % qt4.plugindir)

    pisitools.dodoc("AUTHORS", "COPYING*")
