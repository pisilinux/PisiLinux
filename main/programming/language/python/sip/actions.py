#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(),  get.srcVERSION())
py2dir = get.curPYTHON()
py3dir = "python3.4"

def setup():
    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s" % WorkDir,  "build_python3")
    shelltools.cd(WorkDir)
    pythonmodules.run('configure.py \
                    -b /usr/bin \
                    -d /usr/lib/%s/site-packages \
                    -e /usr/include/%s \
                    CFLAGS+="%s" CXXFLAGS+="%s"' % (py2dir, py2dir, get.CFLAGS(), get.CXXFLAGS()))

    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.run('configure.py \
                    -b /usr/bin \
                    -d /usr/lib/%s/site-packages \
                    -e /usr/include/%s \
                    CFLAGS="%s" CXXFLAGS="%s"' % (py3dir, py3dir, get.CFLAGS(), get.CXXFLAGS()), pyVer = "3")

def build():
    autotools.make()

    shelltools.cd("../build_python3/%s" % WorkDir)
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("LICENSE*", "NEWS", "README")

    shelltools.cd("../build_python3/%s" % WorkDir)
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
