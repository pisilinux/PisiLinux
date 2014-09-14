#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-src" % get.srcDIR()

datadir="/usr/share/boswars"

def fixperms(d):
    import os

    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    # if upstream forgets, don't forget to add -fsigned-char to flags
    pisitools.dosed("SConstruct", "-O2 -pipe -fomit-frame-pointer -fexpensive-optimizations -ffast-math", \
                                  "%s -fexpensive-optimizations -ffast-math" % get.CXXFLAGS())
def build():
    scons.make('CC="%s" CXX="%s"' % (get.CC(), get.CXX()))

def install():
    pisitools.dobin("boswars")

    pisitools.dodir(datadir)
    for files in ["campaigns", "graphics", "languages", "maps", \
                  "scripts", "sounds", "units", "intro"]:
        fixperms(files)
        shelltools.copytree(files, "%s/%s/" % (get.installDIR(), datadir))

    pisitools.insinto("/usr/share/doc/%s/scripts" % get.srcNAME(), "doc/scripts/*.py")
    pisitools.dohtml("doc/*", "doc/scripts/*")
    pisitools.dodoc("CHANGELOG", "*.txt", "doc/*.txt")
