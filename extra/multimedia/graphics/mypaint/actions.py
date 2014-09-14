#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    scons.make()

def install():
    scons.install("prefix=%s/usr install" % get.installDIR())

    pisitools.dodoc("changelog", "COPYING", "LICENSE", "README", "doc/*" )

