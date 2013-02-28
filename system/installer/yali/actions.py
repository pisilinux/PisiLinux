#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    repo_uri = "http://packages.pardus.org.tr/pardus/2011.2/devel/%s/pisi-index.xml.xz" % get.ARCH()
    pisitools.dosed("yali/constants.py", "@REPO_URI@", repo_uri)

    pisitools.dosed("conf/yali.conf", "@INSTALL_TYPE@", "system")

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
