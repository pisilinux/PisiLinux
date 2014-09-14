#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    perlmodules.configure()
    shelltools.system("rm -rf perl-modules")

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.dodoc("Changes*", "COPYRIGHT", "Credits", "README", "TODO")