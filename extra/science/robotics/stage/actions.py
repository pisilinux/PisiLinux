#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

WorkDir = "rtv-Stage-c318423"

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    # No need to package test programs
    pisitools.removeDir("/usr/bin")

    pisitools.dodoc("AUTHORS*", "README*", "RELEASE*", "todo*")
