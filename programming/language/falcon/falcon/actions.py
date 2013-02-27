#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

WorkDir = "Falcon-%s" % get.srcVERSION()

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.install()
