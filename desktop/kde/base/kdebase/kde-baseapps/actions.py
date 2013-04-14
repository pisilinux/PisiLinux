#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())
NoStrip=["/usr/share/icons"]

def setup():
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()

    shelltools.move("../pics/*.png", "%s/usr/share/kde4/apps/kdm/pics/users" % get.installDIR())
    #this file exceeds 20K limit of kdm, and KDM cannot display that.
    pisitools.remove("/usr/share/kde4/apps/kdm/pics/users/Happy.png")
