#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4


def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    pisitools.dobin("diffpdf")
    pisitools.doman("diffpdf.1")

    pisitools.dodoc("CHANGES", "gpl-2.0.txt", "README*")
