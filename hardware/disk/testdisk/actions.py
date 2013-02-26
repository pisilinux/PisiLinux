#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--enable-sudo")

def build():
    autotools.make()

def install():
    autotools.install()
