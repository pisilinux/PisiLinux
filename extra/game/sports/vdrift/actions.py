#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import get

import os

NoStrip = "/"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)
            if name.startswith("SConscript"):
                shelltools.unlink(os.path.join(root, name))

def setup():
    fixperms("data")


def build():
    scons.make('release=1 \
                destdir="%s" \
                prefix=/usr \
                datadir=share/vdrift \
                bindir=bin \
                localedir=share/locale \
                NLS=0 \
                use_binreloc=0' % get.installDIR())

def install():
    pisitools.dobin("build/vdrift")
    pisitools.dodir("/usr/share")
    shelltools.copytree("data", "%s/usr/share/vdrift" % get.installDIR())

    pisitools.dodoc("LICENSE", "README*")


