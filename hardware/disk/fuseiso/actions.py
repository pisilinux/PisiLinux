#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
