#!    pisitools.remove("bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-if")
    autotools.configure("--disable-scrollkeeper                                \
                         --disable-schemas-compile                             \
                         --with-gtk=2.0                                        \
                         --with-x                                              \
                         --disable-static                                      \
                         --enable-unique                                       \
                         --enable-gtk-doc                                      \
                         --with-pnp-ids-path=/usr/share/hwdata/pnp.ids         \
                         --with-omf-dir=/usr/share/omf/mate-desktop            \
                         --enable-gnucat")

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())