#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-scores-group=users \
                         --with-scores-user=root")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.domove("/var/games/gweled.Normal.scores", "/var/state/gweled/")
    pisitools.domove("/var/games/gweled.Timed.scores", "/var/state/gweled/")
    pisitools.removeDir("/var/games")

    pisitools.dodoc("AUTHORS", "NEWS", "ChangeLog", "COPYING")
