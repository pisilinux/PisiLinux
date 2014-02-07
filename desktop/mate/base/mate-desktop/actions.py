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
    pisitools.dosed("schemas/org.mate.background.gschema.xml.in.in", "backgrounds/mate/desktop/Stripes.png", "backgrounds/mate/nature/pisi.jpg")
    autotools.configure("--disable-scrollkeeper                                \
                         --disable-schemas-compile                             \
                         --with-gtk=2.0                                        \
                         --with-x                                              \
                         --disable-static                                      \
                         --enable-unique                                       \
                         --enable-gtk-doc                                      \
                         --with-pnp-ids-path=/usr/share/hwdata/pnp.ids         \
                         --with-omf-dir=/usr/share/omf/mate-desktop            ")

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # remove needless gsettings convert file to avoid slow session start
    pisitools.removeDir("/usr/share/MateConf")
