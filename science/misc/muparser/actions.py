#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="%s_v132" % get.srcNAME()

def setup():
    autotools.configure("--enable-shared \
                         --enable-samples=no \
                         --enable-debug=no")

def build():
    autotools.make()


def install():
    autotools.install()

    pisitools.dodoc("Changes.txt", "Credits.txt", "License.txt")
