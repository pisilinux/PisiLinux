#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("pdb2pqr-wrapper", "@PYTHONDIR@", "/usr/lib/%s" % get.curPYTHON())
    shelltools.chmod("pdb2pqr-wrapper", 0755)

    autotools.configure("--enable-propka \
                         --enable-pdb2pka")

def build():
    autotools.make()

def install():
    pdb2pqrdir = "/usr/lib/%s/site-packages/%s" % (get.curPYTHON(), get.srcNAME())
    pisitools.insinto(pdb2pqrdir, "*.py")
    pisitools.insinto("/usr/bin", "pdb2pqr-wrapper", "pdb2pqr")

    shelltools.copytree("extensions", "%s/%s" % (get.installDIR(), pdb2pqrdir))
    shelltools.copytree("dat", "%s/%s" % (get.installDIR(), pdb2pqrdir))
    shelltools.copytree("src", "%s/%s" % (get.installDIR(), pdb2pqrdir))

    #create freemol directory and symlink, some programs (like pymol) may look here to source python file directly
    pydir = "/usr/lib/%s/site-packages/" % get.curPYTHON()
    pisitools.dodir("%s/pymol/freemol/bin" % pydir)
    pisitools.dosym("%s/pdb2pqr/pdb2pqr.py" % pydir, "%s/pymol/freemol/bin/pdb2pqr.py" % pydir)

    pisitools.dodoc("ChangeLog", "NEWS", "COPYING")
