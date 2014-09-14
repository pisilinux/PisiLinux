#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    for size in ["16", "32", "64"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (size, size) , \
                "artwork/%s-icon-%s.png" % (get.srcNAME(),size) , "%s.png" % get.srcNAME())

    pisitools.insinto("/usr/share/icons/hicolor/scalable/apps", \
            "artwork/%s-icon.svg" % get.srcNAME(), "%s.svg" % get.srcNAME())

    shelltools.chmod("%s/usr/lib/%s/site-packages/*.py" % (get.installDIR(), get.curPYTHON()))
