#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "dvdbackup"

def build():
    autotools.compile("-I/usr/include/dvdread -o dvdbackup src/dvdbackup.c -ldvdread")

def install():
    pisitools.dobin("dvdbackup")
