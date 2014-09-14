#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

resources_dir = "/usr/share/btanks"
lib_dir = "/usr/lib/btanks"

NoStrip = [resources_dir]

def build():
    scons.make("prefix=/usr \
                resources_dir=%s \
                lib_dir=%s \
                plugins_dir=%s \
                enable_lua=yes \
                mode=release" % (resources_dir, lib_dir, lib_dir))

def install():
    pisitools.dobin("build/release/engine/btanks")
    pisitools.dobin("build/release/editor/bted")
    pisitools.rename("/usr/bin/bted", "btanks-editor")

    for _so in ("clunk/libclunk.so", "engine/libbtanks_engine.so", "sdlx/libsdlx.so",
                "objects/libbt_objects.so", "mrt/libmrt.so"):
        pisitools.doexe("build/release/%s" % _so, lib_dir)

    for files in ["data/*.xml", "data/playlist"]:
        pisitools.insinto(resources_dir, files)

    for data in ("data/font", "data/maps", "data/sounds",
                 "data/tiles", "data/tilesets", "data/tunes"):
        shelltools.copytree(data, "%s/%s" % (get.installDIR(), resources_dir))

    pisitools.dodoc("ChangeLog", "LICENSE*", "*.txt")
