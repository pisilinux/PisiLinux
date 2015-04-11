#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="PyQt-gpl-%s" % get.srcVERSION()

def setup():
    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s" % WorkDir,  "build_python3")
    shelltools.cd(WorkDir)
     
    pythonmodules.run("configure.py --confirm-license \
                                    --no-timestamp \
                                    --assume-shared \
                                    --qsci-api \
                                    -q /usr/lib/qt5/bin/qmake")
    shelltools.system("find -name 'Makefile' | xargs sed -i 's|-Wl,-rpath,/usr/lib||g;s|-Wl,-rpath,.* ||g'")

    shelltools.cd("../build_python3/%s" % WorkDir)
    pythonmodules.run("configure.py --sip-incdir='/usr/include/python3.4' --confirm-license -q /usr/lib/qt5/bin/qmake", pyVer = "3")
    shelltools.system("find -name 'Makefile' | xargs sed -i 's|-Wl,-rpath,/usr/lib||g;s|-Wl,-rpath,.* ||g'")

def build():
    autotools.make("-C pyrcc")
    shelltools.cd("../build_python3/%s" % WorkDir)
    autotools.make("-C pylupdate")

def install():
    pisitools.insinto("/usr/share/qt/qsci/api/python", "PyQt5.api")
    shelltools.cd("../build_python3/%s" % WorkDir)
    autotools.rawInstall("DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    pisitools.rename("/usr/bin/pyuic5", "pyuic5-python3")

    shelltools.cd("../../%s" % WorkDir)
    autotools.rawInstall("DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("NEWS", "README", "LICENSE*")
