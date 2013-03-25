#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    for f in ("yali/constants.py", "yali/storage/bootloader.py", "yali/storage/__init__.py"):
        pisitools.dosed(f, "pardus-release", "pisilinux-release")

    pisitools.dosed("yali/gui/Ui/exception.ui", "bugs.pardus.org.tr", r"bugs.pisilinux.org")

    pisitools.dosed("yali/postinstall.py", "(yali-(theme|branding)-)pardus", r"\1pisilinux")
    pisitools.dosed("yali-bin", '(default=")pardus', r'\1pisilinux')

    repo_uri = "http://anka.pardus-linux.org/2013/anka/repos/alpha/pisi-index.xml.xz" # FIXME
    pisitools.dosed("yali/constants.py", "@REPO_URI@", repo_uri)
    pisitools.dosed("yali/constants.py", "@REPO_NAME@", "pisi01") # FIXME

    pisitools.dosed("conf/yali.conf", "@INSTALL_TYPE@", "system")

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
