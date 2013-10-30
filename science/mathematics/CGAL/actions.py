#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import Error

import os
from stat import *


def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release",installPrefix="/usr")


def build():
    cmaketools.make()

    #these wont compile with our boost
    #obsolotes = ["demo/Mesh_3", "demo/Polyhedron", "examples/Mesh_3", "examples/Polyhedron"]
    cmaketools.make("demos")
    cmaketools.make("examples")


def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/usr/lib/CGAL")

    pisitools.dohtml("doc_html/")

    pisitools.insinto("/usr/share/CGAL/examples", "examples/*")

    # copy executables only
    for i in ["demo", "examples"]:
        for root, dirs, files in os.walk(i):
            for filename in files:
                curfile = os.path.join(root, filename)
                if os.stat(curfile)[ST_MODE] & S_IXUSR:
                    pisitools.insinto("/usr/share/CGAL/%s" % curfile, curfile)