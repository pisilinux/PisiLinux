#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))

def setup():
    autotools.configure("\
                         --with-modulesdir=/usr/lib/ldb/modules \
                         --with-privatelibdir=/usr/lib/ldb \
                         --builtin-libraries=replace \
                         --bundled-libraries=NONE \
                         --disable-rpath \
                         --disable-rpath-install \
                        ")

def build():
    shelltools.system("make")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
