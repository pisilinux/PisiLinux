#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

ver = "1.13.1"

def setup():
    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    autotools.make()

#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Use gnuconfig files
    for config in ["config.guess","config.sub"]:
        #pisitools.remove("/usr/share/automake-%s/%s" % (ver, config))
        pisitools.dosym("/usr/share/gnuconfig/%s" % config, "/usr/share/automake-%s/%s" % (ver, config))

    pisitools.dodoc("NEWS", "README", "THANKS","AUTHORS", "ChangeLog*")
