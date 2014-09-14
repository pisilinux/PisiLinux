#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir = "el_linux"
datadir = "/usr/share/eternal-lands"
NoStrip = ["/usr/share/eternal-lands"]

data = ["2dobjects", "3dobjects", "actor_defs", "animations", "languages", "maps", "meshes",
        "particles", "shaders", "skeletons", "skybox", "textures"]


def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    for files in ["3dobjects.txt", "global_filters.txt", "sound_warnings.txt",
                  "*.lst", "*.xml"]:
        pisitools.insinto(datadir, files)

    for f in data:
        shelltools.copytree(f, "%s/%s" % (get.installDIR(), datadir))

    fixperms(get.installDIR())

    pisitools.dodoc("license.txt")
