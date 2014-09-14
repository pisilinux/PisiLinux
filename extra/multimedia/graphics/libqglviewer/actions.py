#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="libQGLViewer-%s" % get.srcVERSION().replace("_", "-")

def setup():
    shelltools.cd("QGLViewer")
    shelltools.system("qmake PREFIX=%s/usr DOC_DIR=%s/usr/share/doc/%s/html" %
            (get.installDIR(), get.installDIR(), get.srcNAME()))

def build():
    shelltools.cd("QGLViewer")
    autotools.make("QMAKE=qmake")

def install():
    shelltools.cd("QGLViewer")
    autotools.rawInstall("PREFIX=%s/usr DESTDIR=%s" % (get.installDIR(), get.installDIR()))

    shelltools.cd("..")
    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "examples" )
    pisitools.dodoc("CHANGELOG", "LICENCE", "README")
