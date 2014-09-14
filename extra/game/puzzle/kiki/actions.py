#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "kiki"
datadir = "/usr/share/kiki"
makeparams = 'OPTFLAGS="%s" PYTHON_VERSION=%s' % (get.CXXFLAGS(), get.curPYTHON().lstrip("python"))

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
            if name == "CVS":
                shelltools.unlinkDir(os.path.join(root, name))
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)
            if name == ".cvsignore" or name.endswith(".dll"):
                shelltools.unlink(os.path.join(root, name))
            #Changes nothing
            #if name.endswith(".py"):
            #    pisitools.dosed(os.path.join(root, name), "\n\r", "\n")

def setup():
    shelltools.unlink("Readme.rtf")
    for f in ["Readme.txt", "Thanks.txt", "uDevGame Readme.txt", "story.txt"]:
        pisitools.dosed(f, "\n\r", "\n")

    pisitools.dosed("py/runkiki", "python2.2", get.curPYTHON())

    # SWIG hell
    shelltools.cd("SWIG")
    shelltools.system("swig -c++ -python -globals kiki -o KikiPy_wrap.cpp KikiPy.i")
    shelltools.copy("kiki.py", "../py/")

def build():
    shelltools.cd("kodilib/linux")
    autotools.make(makeparams)

    shelltools.cd("../../linux")
    autotools.make(makeparams)

def install():
    pisitools.dobin("linux/kiki")

    pisitools.dodir(datadir)
    for d in ["sound", "py"]:
        fixperms(d)
        shelltools.copytree(d, "%s/%s/" % (get.installDIR(), datadir))

    pisitools.dodoc("Readme.txt", "Thanks.txt", "uDevGame Readme.txt", "story.txt")

