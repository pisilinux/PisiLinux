#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#ver = "1.14"

def setup():
    #autotools.autoreconf("-fi")
    autotools.configure()

def build():
    autotools.make()

#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Use gnuconfig files
#    for config in ["config.guess","config.sub"]:
#        pisitools.remove("/usr/share/automake-%s/%s" % (ver, config))
#        pisitools.dosym("/usr/share/gnuconfig/%s" % config, "/usr/share/automake-%s/%s" % (ver, config))

    pisitools.dodoc("NEWS", "README", "THANKS","AUTHORS", "ChangeLog*")
