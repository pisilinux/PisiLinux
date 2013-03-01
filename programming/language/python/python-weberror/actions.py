#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
