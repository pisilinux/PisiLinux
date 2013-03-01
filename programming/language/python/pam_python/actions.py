#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "%s-%s" % (get.srcNAME().replace("_","-"), get.srcVERSION())

def build():
    autotools.make("DESTDIR=%s" % get.installDIR())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README.txt", "ChangeLog.txt", "epl-v10.html")
