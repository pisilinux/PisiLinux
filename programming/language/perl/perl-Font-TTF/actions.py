#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir="Font-TTF-%s" % get.srcVERSION()

def setup():
    for d in ("COPYING", "README.TXT", "TODO", "Changes"):
        shelltools.chmod(d, 0644)

    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("COPYING", "README*", "TODO", "Changes")
