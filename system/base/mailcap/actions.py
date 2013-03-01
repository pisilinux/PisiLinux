#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s sysconfdir=/%s mandir=/%s" % (get.installDIR(), get.confDIR(), get.manDIR()))

    pisitools.dodoc("COPYING", "NEWS")
