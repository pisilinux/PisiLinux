#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    # Compile gbdfed with GTK+ 2.22
    pisitools.dosed("Makefile.in", "-D.*_DEPRECATED.*$")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "NEWS", "README")
