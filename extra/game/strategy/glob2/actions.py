#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

# follow upsream changes through cvs, but prefer tarball
# CVS_RSH="ssh" cvs -z3 -d:pserver:anonymous@cvs.savannah.nongnu.org:/sources/glob2 co -r alpha22-rc glob2
#
# sync data files in case upstream forgets
# rsync -rzv yog.globulation2.org::glob2data data/
# rsync -rzv yog.globulation2.org::glob2maps maps/
# rsync -rzv yog.globulation2.org::glob2campaigns campaigns/


from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import get

import os

datadir = "/usr/share/glob2"

def fixDirs(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)
            if name == "SConscript":
                shelltools.unlink(os.path.join(root,name))

def build():
    scons.make('CXXFLAGS="%s " \
                LINKFLAGS="%s " \
                LINKFLAGS=-lboost_system \
                INSTALLDIR="/usr/share/glob2"' % (get.CXXFLAGS(), get.LDFLAGS()))


def install():
    pisitools.dobin("src/glob2")
    pisitools.dodir(datadir)

    for d in ["campaigns", "data", "maps", "scripts"]:
        pisitools.insinto(datadir, d)

    fixDirs("%s/%s" % (get.installDIR(), datadir))
    pisitools.dodoc("README*", "COPYING")
