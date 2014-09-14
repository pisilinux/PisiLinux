#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("bin/gscan2pdf", "<http://www.gnu.org/licenses/>", "http://www.gnu.org/licenses/")
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.dodoc("COPYING", "History", "LICENCE")
