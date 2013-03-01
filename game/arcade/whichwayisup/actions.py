#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "whichwayisup"

def install():
    pisitools.insinto("/usr/share/whichwayisup", "./*")
    pisitools.removeDir("/usr/share/whichwayisup/data/misc")
    pisitools.removeDir("usr/share/whichwayisup/data/music")
    pisitools.remove("/usr/share/whichwayisup/changelog.txt")
    pisitools.remove("/usr/share/whichwayisup/README.txt")
    pisitools.remove("/usr/share/whichwayisup/cmd_here.bat")
    shelltools.chmod("%s/usr/share/whichwayisup/run_game.py" % get.installDIR())
    shelltools.chmod("%s/usr/share/whichwayisup/lib/*" % get.installDIR(),0644)
    shelltools.chmod("%s/usr/share/whichwayisup/data/*" % get.installDIR(),0644)
    shelltools.chmod("%s/usr/share/whichwayisup/data/sounds/*" % get.installDIR(),0644)
    shelltools.chmod("%s/usr/share/whichwayisup/data/levels/*" % get.installDIR(),0644)
    shelltools.chmod("%s/usr/share/whichwayisup/data/pictures/*" % get.installDIR(),0644)
    pisitools.dosym("/usr/share/whichwayisup/run_game.py", "/usr/bin/whichwayisup")
    pisitools.dodoc("README.txt")
