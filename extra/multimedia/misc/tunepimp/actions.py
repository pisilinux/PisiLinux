#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i -e 's, mp4,,' plugins/Makefile.am")
    shelltools.system("sed -i -e 's,mp4v2,mp4v3,' configure.in")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("python/")
    pythonmodules.install()
    shelltools.cd("..")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")