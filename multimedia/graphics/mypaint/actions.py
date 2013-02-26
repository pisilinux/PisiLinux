#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    scons.make()

def install():
    scons.install("prefix=%s/usr install" % get.installDIR())

    pisitools.dodoc("changelog", "COPYING", "LICENSE", "README", "doc/*" )

