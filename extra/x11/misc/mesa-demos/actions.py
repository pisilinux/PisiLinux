# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

demos_dir = "/usr/lib/mesa/demos"
demos_dir_emul32 = "/usr/lib32/mesa/demos"

def setup():
    autotools.autoreconf("-fvi")
    options = "--disable-static \
               --with-system-data-files \
               --bindir=%s" % (demos_dir_emul32 if get.buildTYPE() == "emul32" else demos_dir)

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
        pisitools.dobin("src/egl/opengl/xeglgears")
