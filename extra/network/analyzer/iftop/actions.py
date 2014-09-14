#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dosbin("iftop")
    pisitools.doman("iftop.8")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "COPYING")
