#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("make.sh", "gcc", get.CC())

def build():
    shelltools.system("./make.sh")

def install():
    pisitools.dobin("unpaper")

    pisitools.dodoc("CHANGELOG", "LICENSE", "README")
    pisitools.insinto("%s/unpaper" % get.docDIR(), "doc/*")
