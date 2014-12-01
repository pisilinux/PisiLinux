#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

configTemplateDir = "/usr/share/libtool/config"

def setup():
    #pisitools.cflags.add("-fPIC")
    #autotools.configure("--enable-static=no")
    autotools.configure()


def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for f in ["config.sub", "config.guess"]:
        pisitools.remove("%s/%s" % (configTemplateDir, f))
        pisitools.dosym("/usr/share/gnuconfig/%s" % f, "%s/%s" % (configTemplateDir, f))

    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "NEWS", "README", "THANKS", "doc/PLATFORMS")

