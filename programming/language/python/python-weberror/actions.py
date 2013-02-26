#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "WebError-%s" % get.srcVERSION()

EggDir = "/usr/lib/%s/site-packages/%s-py2.7.egg-info" % (get.curPYTHON(), WorkDir)

def install():
    pythonmodules.install()

    pisitools.remove("%s/requires.txt" % EggDir)
    pisitools.remove("%s/entry_points.txt" % EggDir)
    pisitools.remove("%s/top_level.txt" % EggDir)
