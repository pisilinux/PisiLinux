#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("CXX=%s" % get.CXX())

def install():
    pisitools.dobin("pbzip2")
    pisitools.doman("pbzip2.1")

    pisitools.dosym("pbzip2", "/usr/bin/pbunzip2")
    pisitools.dosym("pbzip2", "/usr/bin/pbzcat")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
