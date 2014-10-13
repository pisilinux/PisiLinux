#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/onyx/work/ and:
# WorkDir="onyx-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    pisitools.insinto("/usr/share/onyx/", "onyx-1.0.jar")

#def build():
    #autotools.make()

def install():
    pisitools.insinto("/usr/share/onyx/", "onyx-1.0.jar")
    pisitools.insinto("/usr/share/onyx/", "onyx.sh")
    pisitools.dosym("/usr/share/onyx/onyx.sh", "/usr/bin/onyx")
   