#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "%s-%s-pngonly" % (get.srcNAME(), get.srcVERSION())
ClipartDir = "/usr/share/clipart/%s" % get.srcNAME()
NoStrip=["/"]

def install():
    #Since installDIR is created just before this function, I can't do those 2 operations in setup function :/
    shelltools.makedirs("%s/%s" % (get.installDIR(), ClipartDir))
    pisitools.dosym(get.srcNAME(), "%s-%s" % (ClipartDir, get.srcVERSION()))

    shelltools.cd("clipart")

    for d in shelltools.ls("."):
        if os.path.isdir("%s/%s/clipart/%s" % (get.workDIR(), WorkDir, d)):
            print "Copying '%s' to %s/%s/%s" % (d, get.installDIR(), ClipartDir, d)
            shelltools.copytree(d, "%s/%s/%s" % (get.installDIR(), ClipartDir, d))

    #Clear non-png files
    for root, dirs, files in os.walk("%s/%s" % (get.installDIR(), ClipartDir)):
        for name in files:
            if not name.endswith(".png"):
                f = os.path.join(root, name)
                print "Removing non-png file '%s'" % f
                shelltools.unlink(f)

    shelltools.cd("..")

    pisitools.dodoc("AUTHORS", "ChangeLog", "LICENSE", "NEWS", "README", "VERSION")
