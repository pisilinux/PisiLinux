#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4

def setup():
    qt4.configure(parameters="CONFIG+=QwtSVGItem")

def build():
    qt4.make()


def install():
    qt4.install()

    pisitools.doman("doc/man/*/*")
    pisitools.dohtml("doc/html/*")

    pisitools.rename("/usr/share/man/man3/deprecated.3", "qwt-deprecated.3")

    pisitools.insinto("/usr/share/doc/qwt/examples", "examples")
