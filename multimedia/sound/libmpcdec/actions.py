#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
import os

def setup():
    # This is a very important workaround / fix
    os.system('touch -d "15 March 1980" configure.ac')

    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
