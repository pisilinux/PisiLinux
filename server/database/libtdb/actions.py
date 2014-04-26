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
                         --builtin-libraries=replace \
                         --bundled-libraries=NONE \
                         --disable-rpath \
                        ")

def build():
    shelltools.system("make")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("docs/README")
