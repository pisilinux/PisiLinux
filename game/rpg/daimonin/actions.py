#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir = "daimonin/client/make/linux"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    shelltools.chmod("configure", 0755)
    autotools.configure("-disable-simplelayout")

def build():
    autotools.make("all")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    fixperms("%s/usr/share/daimonin" % get.installDIR())

    # we remove this from makefile, keeping it for now
    # pisitools.remove("/usr/bin/updater")

    pisitools.dodoc("README")
