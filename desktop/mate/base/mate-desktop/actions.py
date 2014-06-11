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
    #Change default xcursor
    pisitools.dosed("schemas/org.mate.peripherals-mouse.gschema.xml.in.in", "<default>''</default>", "<default>'mate'</default>")
    pisitools.dosed("schemas/org.mate.background.gschema.xml.in.in", "backgrounds/mate/desktop/Stripes.png", "backgrounds/mate/nature/pisi.jpg")
    autotools.configure("--prefix=/usr \
                         --with-gtk=2.0 \
                         --enable-mpaste \
                         --disable-static \
                         --disable-schemas-compile \
                         --disable-desktop-docs \
                         --enable-gtk-doc")

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # remove needless gsettings convert file to avoid slow session start
    pisitools.removeDir("/usr/share/MateConf")
