#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # change slider direction
    pisitools.dosed("yali/gui/Ui/", "RightToLeft", "LeftToRight", filePattern="^(logicalvolume|partition)\..*")

    # let progressbar starts from 0
    pisitools.dosed("yali/gui/Ui/installprogress.ui", ">65<", ">0<")

    repo_uri = "http://packages.pisilinux.org/repositories/1.0/stable/x86_64/pisi-index.xml.xz" # FIXME
    pisitools.dosed("yali/constants.py", "@REPO_URI@", repo_uri)
    pisitools.dosed("yali/constants.py", "@REPO_NAME@", "pisi") # FIXME

    pisitools.dosed("conf/yali.conf", "@INSTALL_TYPE@", "system")

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
