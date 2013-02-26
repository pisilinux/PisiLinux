# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

demos_dir = "/usr/lib/mesa/demos"
demos_dir_emul32 = "/usr/lib32/mesa/demos"

shelltools.export("LDFLAGS", "%s -lX11 -lGL -lm -lpthread" % get.LDFLAGS())

def setup():
    options = "--bindir=%s \
               --disable-static" % demos_dir

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=%s" % demos_dir_emul32
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        for util in ("glxgears", "glxinfo"):
            pisitools.domove("%s/%s" % (demos_dir_emul32, util), "/usr/bin/", "%s32" % util)
        return

    for util in ("glxgears", "glxinfo"):
        pisitools.domove("%s/%s" % (demos_dir, util), "/usr/bin/")
