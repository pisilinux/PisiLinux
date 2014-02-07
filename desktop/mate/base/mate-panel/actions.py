 #!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #çalışma alanını 2 satırda gösterir.
    pisitools.dosed("applets/wncklet/org.mate.panel.applet.workspace-switcher.gschema.xml.in.in", "1", "2")
    autotools.configure("--disable-scrollkeeper                 \
                         --disable-static                       \
                         --disable-schemas-compile              \
                         --with-x                               \
                         --libexecdir=/usr/lib/mate-panel       \
                         --enable-introspection")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/mate-panel/", "data/panel-default-layout.mate", "panel-default-layout.dist")

    # remove needless gsettings convert file to avoid slow session start
    pisitools.removeDir("/usr/share/MateConf")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
