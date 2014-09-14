#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    # rdfpipe does not work without egg-info files, please do not remove it!
    #pisitools.removeDir("/usr/lib/%s/site-packages/rdflib-%s-py%s.egg-info" % (get.curPYTHON(), get.srcVERSION(), get.curPYTHON().replace("python", "")))
