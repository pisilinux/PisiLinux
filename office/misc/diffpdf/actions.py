#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt4


def setup():
    shelltools.system("lrelease diffpdf_cz.ts diffpdf_cz.qm")
    shelltools.system("lrelease diffpdf_de.ts diffpdf_de.qm")
    shelltools.system("lrelease diffpdf_fr.ts diffpdf_fr.qm")
    qt4.configure()

def build():
    qt4.make()

def install():
    pisitools.dobin("diffpdf")
    pisitools.doman("diffpdf.1")

    pisitools.dodoc("CHANGES", "gpl-2.0.txt", "README*")
