#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir= "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("0.0_", ""))

def setup():
    autotools.configure("--enable-static=no")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc('AUTHORS', 'README', 'NEWS', 'ChangeLog')
