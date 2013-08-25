#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))
shelltools.export("LC_ALL", "C")

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --enable-nls \
                            --update-po \
                            --enable-docs \
                            --enable-apidocs  \
                            --enable-unique \
                            --disable-gtk3 \
                            --enable-addons")

def build():
    shelltools.system("make")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/gir-1.0")

