#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools


def setup():
    # Fix doc dir
    pisitools.dosed("CMakeLists.txt", "(.*share\/)(luminance-hdr.*info\sfiles.*)", r"\1doc/\2")
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.install()
