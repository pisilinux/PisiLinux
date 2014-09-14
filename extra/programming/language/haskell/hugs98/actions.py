#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

from datetime import date
import os

year, month = get.srcVERSION().split(".")
WorkDir = "hugs98-plus-%s%s" % (date(1, int(month), 1).ctime()[4:7], year)

hugsdir = "/usr/lib/hugs"

def setup():
    #pisitools.dosed("packages/GLUT/GLUT.buildinfo.in", "@GLUT_LIBS@", "-lglut  -lSM -lICE -lXmu -lXi  -lGLU -lGL -lm")
    #pisitools.dosed("packages/OpenGL/OpenGL.buildinfo.in", "@GLU_LIBS@", "-lGLU -lGL -lm")

    shelltools.export("hugsdir", hugsdir)
    autotools.configure("--enable-ffi \
                         --enable-profiling \
                         --enable-char-encoding=utf8 \
                         --enable-opengl")

def build():
    autotools.make()

    pisitools.dosed("hugsdir/programs/hsc2hs/Paths_hsc2hs.hs", r"^(datadir *= *).*", r'\1"%s/programs/hsc2hs"' % hugsdir)

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for root, dirs, files in os.walk("%s/%s" % (get.installDIR(), hugsdir)):
        libs = [x for x in files if x.endswith(".so")]
        for lib in libs:
            shelltools.chmod("%s/%s" % (root, lib), 0755)

    pisitools.domove("%s/docs/*" % hugsdir, "%s/%s" % (get.docDIR(), get.srcNAME()))
    pisitools.domove("%s/demos"  % hugsdir, "%s/%s" % (get.docDIR(), get.srcNAME()))

    pisitools.removeDir("%s/docs" % hugsdir)
    pisitools.remove("%s/Credits" % hugsdir)
    pisitools.remove("%s/License" % hugsdir)
    pisitools.remove("%s/Readme"  % hugsdir)

    pisitools.dodoc("Credits", "License", "Readme")
