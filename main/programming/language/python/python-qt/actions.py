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

WorkDir="PyQt-x11-gpl-%s" % get.srcVERSION()

def setup():
    shelltools.cd("..")
    shelltools.makedirs("build_python3")
    shelltools.copytree("./%s" % WorkDir,  "build_python3")
    shelltools.cd(WorkDir)

    pisitools.dosed("configure.py", "  check_license()", "# check_license()")
    pythonmodules.run("configure.py -q /usr/bin/qmake")

    shelltools.cd("../build_python3/%s" % WorkDir)
    pisitools.dosed("configure.py", "  check_license()", "# check_license()")
    pythonmodules.run("configure.py  --verbose -q /usr/bin/qmake", pyVer = "3")

def build():
    autotools.make()
    shelltools.cd("../build_python3/%s" % WorkDir)
    autotools.make()

def install():
    shelltools.cd("../build_python3/%s" % WorkDir)
    autotools.rawInstall("DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    pisitools.rename("/usr/bin/pyuic4", "pyuic4-python3")

    shelltools.cd("../../%s" % WorkDir)
    autotools.rawInstall("DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("NEWS", "README", "THANKS", "LICENSE*", "GPL*", "OPENSOURCE*")
